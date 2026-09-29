SELECT
    *
FROM
    mart_company_leaderboard
LIMIT 20;

SELECT
    clean_company_name,
    remote_jobs,
    remote_percentage,
    avg_salary,
    total_jobs
FROM
    mart_company_leaderboard
ORDER BY
    remote_jobs DESC
LIMIT 20;

SELECT
    COUNT(*) AS null_company_count
FROM
    mart_company_leaderboard
WHERE
    company_id IS NULL
    OR clean_company_name IS NULL
    OR total_jobs IS NULL;


SELECT
    *
FROM
    mart_company_leaderboard
WHERE
    remote_jobs + onsite_jobs > total_jobs;

SELECT
    clean_company_name,
    total_jobs,
    remote_jobs,
    onsite_jobs,
    remote_percentage,
    known_salary_jobs,
    avg_salary
FROM
    mart_company_leaderboard
ORDER BY
    total_jobs DESC
LIMIT 20;