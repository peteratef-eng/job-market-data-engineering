---Task #16
SELECT
    jpf.job_title_short AS job_name,
    sd.skills AS skill_name,
    COUNT(DISTINCT(jpf.job_id)) AS demand_count
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON  sjd.skill_id = sd.skill_id
GROUP BY
    jpf.job_title_short,
    sd.skills
ORDER BY  
    job_name ASC,
    demand_count DESC;