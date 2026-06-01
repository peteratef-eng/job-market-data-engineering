SELECT
    *
FROM
    mart_remote_work_trends
LIMIT 20;

SELECT
    *
FROM
    mart_remote_work_trends
WHERE
    posted_month IS NULL
    OR job_title_short IS NULL
    OR remote_status IS NULL
    OR total_jobs IS NULL;


SELECT
    *
FROM
    mart_remote_work_trends
WHERE
    job_title_short = 'Data Engineer'
ORDER BY
    posted_month, remote_status;


SELECT
    posted_month,
    job_title_short,
    ROUND(SUM(remote_status_percentage), 2) AS percentage_sum
FROM
    mart_remote_work_trends
GROUP BY    
    posted_month,
    job_title_short
HAVING
    ROUND(SUM(remote_status_percentage), 2) NOT BETWEEN 99.9 AND 100.1;