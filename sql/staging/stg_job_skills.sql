CREATE OR REPLACE TEMP VIEW stg_job_skills AS 

SELECT
    skill_id,
    job_id
FROM
    skills_job_dim;



