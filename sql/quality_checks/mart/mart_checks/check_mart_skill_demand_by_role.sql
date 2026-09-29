---CHECK ROWS
SELECT
    *
FROM
    mart_skill_demand_by_role
LIMIT 20;

SELECT
    job_title_short,
    COUNT(*) AS total_skill_rows
FROM
    mart_skill_demand_by_role
GROUP BY
    job_title_short
ORDER BY
    total_skill_rows DESC;

SELECT
    *
FROM
    mart_skill_demand_by_role
WHERE
    clean_skill_name IS NULL
    OR 
    clean_skill_type IS NULL
    OR 
    demand_count IS NULL;


SELECT
    *
FROM
    mart_skill_demand_by_role
WHERE
    job_title_short = 'Data Engineer'
ORDER BY
    demand_count DESC
LIMIT 20;