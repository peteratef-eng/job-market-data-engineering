CREATE OR REPLACE TEMP VIEW int_job_postings_enriched AS

SELECT

    sjp.job_id,
    sjp.company_id,
    sjp.job_title_short,

    sjp.clean_job_title,
    sjp.clean_job_location,
    sjp.remote_status,

    sjp.job_posted_date,
    sjp.posted_month,
    sjp.salary_year_avg,

    sjp.salary_category,
    sc.clean_company_name

FROM
    stg_job_postings AS sjp

LEFT JOIN stg_companies AS sc
    ON sjp.company_id = sc.company_id;

