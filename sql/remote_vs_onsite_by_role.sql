---Task #20
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
    jpf.job_title_short AS job_name,
    jpf.job_work_from_home AS remotely_job,
    COUNT(DISTINCT job_id) AS total_jobs,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary
FROM
    job_postings_fact AS jpf
WHERE
    jpf.salary_year_avg IS NOT NULL
GROUP BY
    jpf.job_title_short,
    jpf.job_work_from_home
ORDER BY
    job_title_short ASC,
    job_work_from_home DESC
LIMIT
    20;