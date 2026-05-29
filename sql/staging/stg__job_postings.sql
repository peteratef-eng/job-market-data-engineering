CREATE OR REPLACE TEMP VIEW stg_job_postings AS 

SELECT
    job_id,
    company_id,
    job_title_short,

    LOWER(TRIM(job_title)) AS clean_job_title,

    COALESCE(NULLIF(TRIM(job_location), ''), 'Unknown') AS clean_job_location,

   (
    CASE
        WHEN job_location IS NULL OR TRIM(job_location) = '' THEN 'Unknown'
        WHEN TRIM(job_location) = 'Anywhere' THEN 'Remote'
        ELSE 'Onsite'
    END
    ) AS remote_status,

    job_posted_date,

    DATE_TRUNC('month', job_posted_date) AS posted_month,

    salary_year_avg,

    (
        CASE
            WHEN salary_year_avg IS NULL THEN 'Unknown'
            WHEN salary_year_avg >= 150_000 THEN 'High Salary'
            WHEN salary_year_avg >= 80_000 THEN 'Medium Salary'
            ELSE 'Low Salary'
        END
    ) AS salary_category

FROM 
    job_postings_fact;

