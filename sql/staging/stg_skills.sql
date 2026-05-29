CREATE OR REPLACE TEMP VIEW stg_skills AS

SELECT
    skill_id,
    skills AS original_skill_name,

    COALESCE(
        NULLIF(
            LOWER(
                TRIM(skills)),
                 ''
                ),
                  'unknown skill name'
            ) AS clean_skill_name,
    type AS original_type_name,

    COALESCE(
        NULLIF(
            LOWER(
                TRIM(type)),
                 ''
                ),
                  'unknown skill type'
            ) AS clean_skill_type
FROM    
    skills_dim;

        
