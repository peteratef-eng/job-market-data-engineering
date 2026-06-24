SELECT
    ijp.job_title_short,
    ijs.clean_skill_name,
    ijs.clean_skill_type,
    COUNT(DISTINCT(ijp.job_id)) AS demand_count
FROM
    {{ ref('int_job_postings_enriched') }} AS ijp
JOIN {{ ref('int_job_skills_enriched') }} AS ijs
    ON ijp.job_id = ijs.job_id
GROUP BY
    ijp.job_title_short,
    ijs.clean_skill_name,
    ijs.clean_skill_type
ORDER BY
    ijp.job_title_short,
    demand_count DESC
