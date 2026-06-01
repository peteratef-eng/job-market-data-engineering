CREATE OR REPLACE TEMP VIEW mart_salary_trends AS

SELECT
    remote_status,
    job_title_short,
    posted_month,
    COUNT(DISTINCT(job_id)) AS total_jobs,

    ROUND(AVG(salary_year_avg), 0) AS avg_salary,
    ROUND(MIN(salary_year_avg), 0) AS min_salary,
    ROUND(MAX(salary_year_avg), 0) AS max_salary

FROM
    int_job_postings_enriched
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    remote_status,
    job_title_short,
    posted_month
ORDER BY
    remote_status,
    job_title_short,
    posted_month;



