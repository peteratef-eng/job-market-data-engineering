SELECT
    COUNT(*)
FROM
    stg_job_skills;

SELECT
    COUNT(*)
FROM    
    skills_job_dim;
    
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) - COUNT(job_id) AS missing_job_id_count,
    COUNT(*) - COUNT(skill_id) AS missing_skill_id_count
FROM
    stg_job_skills;

SELECT
    job_id,
    skill_id,
    COUNT(*) duplicate_count
FROM
    stg_job_skills
GROUP BY
    job_id,
    skill_id   
HAVING 
    COUNT(*) > 1
ORDER BY
    duplicate_count DESC;

SELECT
    sjs.job_id,
    COUNT(*) AS total_skill_links
FROM
    stg_job_skills AS sjs
LEFT JOIN stg_job_postings AS sjp
    ON sjs.job_id = sjp.job_id
WHERE
    sjp.job_id IS NULL
GROUP BY 
    sjs.job_id
ORDER BY
    total_skill_links DESC;


SELECT
    sjs.skill_id,
    COUNT(*) AS total_job_links
FROM
    stg_job_skills AS sjs
LEFT JOIN stg_skills AS ss
    ON sjs.skill_id = ss.skill_id
WHERE
    ss.skill_id IS NULL
GROUP BY
    sjs.skill_id
ORDER BY
    total_job_links DESC;



SELECT
    COUNT(*) 
FROM
    skills_job_dim;

SELECT
    COUNT(*)
FROM
    stg_job_skills;

