SELECT
    *
FROM
    mart_monthly_job_trends
LIMIT 20;

SELECT
    * 
FROM    
    mart_monthly_job_trends
WHERE   
    posted_month  IS NULL
    OR total_jobs   IS NULL;

SELECT
    posted_month,
    COUNT(*) AS duplcate_month_count
FROM
    mart_monthly_job_trends
GROUP BY
    posted_month
HAVING 
    COUNT(*) > 1;


SELECT
    *
FROM
    mart_monthly_job_trends
WHERE
    previous_month_jobs IS NULL
ORDER BY
    posted_month;