SELECT
    company_id,
    clean_company_name,
    
    COUNT(salary_year_avg) AS known_salary_jobs,
    ROUND(AVG(salary_year_avg)::NUMERIC, 2) AS avg_salary,
    ROUND(MIN(salary_year_avg)::NUMERIC, 2) AS min_salary,
    ROUND(MAX(salary_year_avg)::NUMERIC, 2) AS max_salary,

    COUNT(DISTINCT(job_id)) AS total_jobs,

    SUM(
        CASE
            WHEN remote_status = 'Remote' THEN 1
            ELSE 0
        END
    ) AS remote_jobs,

    SUM(
        CASE
            WHEN remote_status = 'Onsite' THEN 1
            ELSE 0
        END
    ) AS onsite_jobs,

    ROUND(
        SUM(
            CASE
                WHEN remote_status = 'Remote' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(DISTINCT job_id)::NUMERIC,    
        2
    ) AS remote_percentage

FROM
    {{ ref('int_job_postings_enriched') }}
GROUP BY 
    company_id,
    clean_company_name
ORDER BY
    total_jobs DESC
    