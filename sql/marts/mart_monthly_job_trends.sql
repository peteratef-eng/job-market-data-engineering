CREATE OR REPLACE TEMP VIEW mart_monthly_job_trends AS 

WITH monthly_jobs AS (
    SELECT
        posted_month,
        COUNT(DISTINCT job_id) AS total_jobs

    FROM
        int_job_postings_enriched
    GROUP BY
        posted_month
),

monthly_jobs_with_previous AS (
    SELECT
        posted_month,
        total_jobs,

        LAG(total_jobs) OVER(
            ORDER BY posted_month
        ) AS previous_month_jobs
    FROM
        monthly_jobs
)
SELECT
    posted_month,
    total_jobs,
    previous_month_jobs,

    total_jobs - previous_month_jobs AS job_difference,

    ROUND(
        (total_jobs - previous_month_jobs) * 100.0 / previous_month_jobs,
        2
    ) AS job_growth_percentage
FROM
    monthly_jobs_with_previous
ORDER BY
    posted_month;