---Task #17
SELECT
    sd.skills AS skill_name,
    COUNT(DISTINCT jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
    ROUND(MAX(jpf.salary_year_avg), 0) AS max_salary
FROM
    job_postings_fact AS jpf
JOIN  skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN  skills_dim AS sd
    ON  sjd.skill_id = sd.skill_id
WHERE
    jpf.job_work_from_home = TRUE
    AND salary_year_avg IS NOT NULL
GROUP BY
    sd.skills
HAVING
    demand_count >= 10
ORDER BY
    demand_count DESC
LIMIT   
    20;

sheheheds
