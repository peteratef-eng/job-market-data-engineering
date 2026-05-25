---Task #18
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
    cd.name AS company_name,
    jpf.job_title_short AS job_name,
    COUNT(DISTINCT jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg,
    ROUND(MAX(jpf.salary_year_avg), 0) AS max_salary
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON  jpf.company_id = cd.company_id
WHERE
    jpf.salary_year_avg IS NOT NULL
GROUP BY
    cd.name,
    jpf.job_title_short
HAVING
    demand_count >= 3
ORDER BY
    demand_count DESC
LIMIT 
    20;