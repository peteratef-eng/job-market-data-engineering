SELECT
    company_id,
    name AS original_company_name,
        COALESCE(
            NULLIF(
                TRIM(name),
                 ''
                 ),
                  'Unknown Company'
             ) AS clean_company_name
FROM
    company_dim
