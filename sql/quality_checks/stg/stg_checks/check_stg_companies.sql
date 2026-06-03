
SELECT *
FROM stg_companies
LIMIT 10;

---ROW NUMBER CHECK
SELECT
    COUNT(*)
FROM
    company_dim;
----215940

SELECT
    COUNT(*)
FROM
    stg_companies;
---215940

---NULL CHECK
SELECT
    company_id,
    original_company_name,
    clean_company_name
FROM
    stg_companies
WHERE
    clean_company_name = 'unknown company';


SELECT
    clean_company_name
FROM
    stg_companies
WHERE
    clean_company_name LIKE ' %'
    OR clean_company_name LIKE '% ';