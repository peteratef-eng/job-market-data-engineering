CREATE OR REPLACE TEMP VIEW stg_companies AS 

SELECT
    company_id,
    name AS original_company_name,

    LOWER(
        COALESCE(
            NULLIF(
                TRIM(name),
                 ''
                 ),
                  'Unknown Company'
             )
             
        ) AS clean_company_name

FROM
    company_dim;


