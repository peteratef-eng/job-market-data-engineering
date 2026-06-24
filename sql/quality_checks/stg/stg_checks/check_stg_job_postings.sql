
SELECT *
FROM stg_job_postings
LIMIT 20;

SELECT
    COUNT(*) AS raw_rows
FROM
    job_postings_fact;

SELECT
    COUNT(*) AS staging_rows
FROM
    stg_job_postings;

SELECT
    remote_status,
    COUNT(*) AS total_jobs
FROM
    stg_job_postings
GROUP BY
    remote_status
ORDER BY
    total_jobs DESC;

SELECT
    salary_category,
    COUNT(*) AS total_jobs
FROM
    stg_job_postings
GROUP BY
    salary_category
ORDER BY
    total_jobs DESC;


SELECT
    posted_month,
    COUNT(*) AS total_jobs
FROM
    stg_job_postings
GROUP BY
    posted_month
ORDER BY
    posted_month
LIMIT 20;