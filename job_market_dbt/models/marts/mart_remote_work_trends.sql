WITH remote_counts AS (
    SELECT
        remote_status,
        posted_month,
        job_title_short,
        COUNT(DISTINCT(job_id)) AS total_jobs
    FROM
        {{ ref('int_job_postings_enriched') }}
    GROUP BY 
        remote_status,
        posted_month,
        job_title_short
)
SELECT
    remote_status,
    posted_month,
    job_title_short,
    total_jobs,

    SUM(total_jobs) OVER(
        PARTITION BY posted_month, job_title_short
    ) AS monthly_role_total,

    ROUND(
        total_jobs * 100.0 /
        SUM(total_jobs) OVER(
        PARTITION BY posted_month, job_title_short
        ),
        2
    ) AS remote_status_percentage
FROM
    remote_counts
ORDER BY
    posted_month,
    job_title_short,
    remote_status
