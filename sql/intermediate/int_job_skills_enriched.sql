CREATE OR REPLACE TEMP VIEW int_job_skills_enriched AS 

SELECT
    sjs.job_id,
    sjs.skill_id,

    ss.clean_skill_name,
    ss.clean_skill_type

FROM
    stg_job_skills AS sjs

LEFT JOIN stg_skills AS ss
    ON sjs.skill_id = ss.skill_id;

