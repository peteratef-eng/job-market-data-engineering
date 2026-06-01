SELECT *
FROM mart_salary_trends
LIMIT 20;

SELECT
    COUNT(*) AS null_check_count
FROM
    mart_salary_trends
WHERE
    posted_month IS NULL
    OR job_title_short IS NULL
    OR remote_status IS NULL
    OR total_jobs IS NULL
    OR avg_salary IS NULL;

SELECT
    *
FROM
    mart_salary_trends
WHERE
    job_title_short = 'Data Engineer'
ORDER BY
    posted_month,
    remote_status;