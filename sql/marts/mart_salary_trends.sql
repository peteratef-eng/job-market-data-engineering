CREATE OR REPLACE TEMP VIEW mart_salary_trends AS

WITH salary_summary  AS (
    SELECT
        remote_status,
        job_title_short,
        posted_month,

        COUNT(DISTINCT(job_id)) AS total_salary_jobs,

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
),
salary_with_previous AS (
    SELECT
    remote_status,
    job_title_short,
    posted_month,
    total_salary_jobs,
    avg_salary,
    min_salary,
    max_salary,

    LAG(avg_salary) OVER(
            PARTITION BY job_title_short, remote_status
            ORDER BY posted_month
        ) AS previous_month_avg_salary
FROM
    salary_summary
ORDER BY
    job_title_short,
    remote_status,
    posted_month
)
SELECT
    remote_status,
    job_title_short,
    posted_month,
    total_salary_jobs,
    avg_salary,
    min_salary,
    max_salary,
    previous_month_avg_salary,

    avg_salary - previous_month_avg_salary AS salary_difference,

    ROUND(
            ((avg_salary - previous_month_avg_salary) / previous_month_avg_salary) * 100.0,
            2
        ) AS salary_growth_percentage

FROM
    salary_with_previous
ORDER BY
    job_title_short,
    remote_status,
    posted_month;
