---Task #19
/*
---skills_job_dim
        skill_id │ job_id │

---job_postings_fact
 job_id │ company_id │ job_title_short │ salary_rate │ salary_year_avg │ salary_hour_avg
---company_dim
│ company_id │ name │ link_google │ thumbnail│

---skills_dim 
    │ skill_id │   skills   │    type     │
*/

SELECT 
    sd.skills AS skill_name,
    COUNT(DISTINCT jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
    avg_salary * demand_count AS score
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
WHERE
    jpf.salary_year_avg IS NOT NULL
    AND job_title_short = 'Data Analyst'
GROUP BY 
    sd.skills
HAVING
    demand_count >= 10
ORDER BY
    score DESC;