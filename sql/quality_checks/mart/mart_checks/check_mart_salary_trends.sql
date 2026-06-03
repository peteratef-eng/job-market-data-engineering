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
    OR total_salary_jobs IS NULL
    OR avg_salary IS NULL;

SELECT
    posted_month,
    previous_month_avg_salary,
    salary_difference,
    salary_growth_percentage
FROM
    mart_salary_trends
WHERE
    job_title_short = 'Data Engineer'
    AND remote_status <> 'Unknown'
ORDER BY
    posted_month,
    remote_status;

DESCRIBE mart_salary_trends;



SELECT
    *
FROM
    mart_salary_trends
WHERE
    previous_month_avg_salary IS NOT NULL
    AND salary_growth_percentage is null;