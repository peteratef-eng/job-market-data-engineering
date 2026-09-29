-- Check 1: Compare row counts
SELECT
    COUNT(*) AS enriched_rows
FROM 
    int_job_postings_enriched;

SELECT
    COUNT(*) AS staging_job_rows
FROM
    stg_job_postings;

-- Check 2: Missing company names after join
SELECT
    COUNT(*) AS missing_company_name_count
FROM
    int_job_postings_enriched
WHERE
    clean_company_name IS NULL;

-- Check 3: Sample output

SELECT
    *
FROM
    int_job_postings_enriched
LIMIT 20;