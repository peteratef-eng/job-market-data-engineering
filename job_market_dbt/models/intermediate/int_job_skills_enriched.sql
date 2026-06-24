SELECT
    sjs.job_id,
    sjs.skill_id,

    ss.clean_skill_name,
    ss.clean_skill_type

FROM
    {{ ref('stg_job_skills') }} AS sjs

LEFT JOIN {{ ref('stg_skills') }} AS ss
    ON sjs.skill_id = ss.skill_id
