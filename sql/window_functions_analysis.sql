---TASK#25
WITH ranked_jobs AS (
    SELECT  
        job_title_short,
        job_title,
        salary_year_avg,

        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS salary_rank

    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)

SELECT
    job_title_short,
    job_title,
    salary_year_avg,
    salary_rank
FROM ranked_jobs
WHERE salary_rank <= 5;


---TASK#26

WITH rank_companies AS (
    SELECT
        cd.name AS company_name,
        COUNT(jpf.job_id) AS total_jobs

    FROM 
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
    GROUP BY cd.name
)

SELECT
    company_name,
    total_jobs,
    RANK() OVER(
            ORDER BY total_jobs DESC
        ) AS company_rank

FROM rank_companies
ORDER BY company_rank;


---TASK#25

WITH rank_companies AS (
    SELECT 
        cd.name AS company_name,
        COUNT(jpf.job_id) AS total_jobs
    FROM job_postings_fact AS jpf

    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
    
    GROUP BY
        cd.name
)

SELECT
    company_name,
    total_jobs,
    DENSE_RANK() OVER(
        ORDER BY total_jobs DESC
    ) AS company_rank
FROM rank_companies
ORDER BY company_rank;