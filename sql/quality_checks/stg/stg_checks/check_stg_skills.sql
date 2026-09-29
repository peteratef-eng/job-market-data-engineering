SELECT
    *
FROM    
    stg_skills
LIMIT 10;



SELECT
    COUNT(*)
FROM
    skills_dim;
---262

SELECT
    COUNT(*)
FROM 
    stg_skills;
---262

SELECT
    *
FROM    
    stg_skills
WHERE
    clean_skill_name = 'unknown skill name'
    OR clean_skill_type = 'unknown skill type';

SELECT
    *
FROM
    stg_skills
WHERE
    clean_skill_name LIKE ' %'
    OR clean_skill_name LIKE '% '
    OR clean_skill_type LIKE ' %'
    OR clean_skill_type LIKE '% ';