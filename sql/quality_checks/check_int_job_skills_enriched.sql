
SELECT
    COUNT(*)
FROM
    stg_job_skills;

SELECT
    COUNT(*)
FROM
    int_job_skills_enriched;

SELECT
    COUNT(*) AS missing_skill_name
FROM    
    int_job_skills_enriched
WHERE
    clean_skill_name IS NULL;

SELECT
    COUNT(*) AS missing_skill_type
FROM    
    int_job_skills_enriched
WHERE
    clean_skill_type IS NULL;


SELECT
    job_id,
    skill_id,
    COUNT(*) AS duplicate_count
FROM
    int_job_skills_enriched
GROUP BY
    job_id,
    skill_id
HAVING
    COUNT(*) > 1
ORDER BY 
    duplicate_count DESC;

SELECT
    *
FROM 
    int_job_skills_enriched
limit 20;


SELECT
    clean_skill_type,
    COUNT(*) AS total_links
FROM
    int_job_skills_enriched
group by 
    clean_skill_type
ORDER by
    total_links DESC;