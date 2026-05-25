/*
DESCRIBE job_postings_fact;
┌──────────────────────────────────────────┐
│            job_postings_fact             │
│                                          │
│ job_id                integer   not null │
│ company_id            integer            │
│ job_title_short       varchar            │
│ job_title             varchar            │
│ job_location          varchar            │
│ job_via               varchar            │
│ job_schedule_type     varchar            │
│ job_work_from_home    boolean            │
│ search_location       varchar            │
│ job_posted_date    ***timestamp***       │
│ job_no_degree_mention boolean            │
│ job_health_insurance  boolean            │
│ job_country           varchar            │
│ salary_rate           varchar            │
│ salary_year_avg       double             │
│ salary_hour_avg       double             │
└──────────────────────────────────────────┘
*/
SELECT
    DATE_TRUNC('month', job_posted_date) AS posted_month,
    COUNT(job_id) AS total_jobs
FROM
    job_postings_fact
GROUP BY
    posted_month
ORDER BY
    posted_month;

---TASK#36

SELECT
    COUNT(*) AS remote_jobs,
    DATE_TRUNC('month', job_posted_date) AS posted_month
FROM
    job_postings_fact
WHERE
    job_work_from_home = TRUE
GROUP BY
    DATE_TRUNC('month', job_posted_date)
ORDER BY
    posted_month;

---TASK#37
SELECT
    ROUND(AVG(salary_year_avg), 0) AS avg_salary,
    COUNT(salary_year_avg) total_salary_jobs,
    DATE_TRUNC('month', job_posted_date) AS posted_month
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
GROUP BY 
    posted_month
ORDER BY
    posted_month;

---TASK38
SELECT
    job_title_short,
    COUNT(job_id) AS total_jobs,
    DATE_TRUNC('month', job_posted_date) AS posted_month
FROM
    job_postings_fact
WHERE
    job_title_short = 'Data Analyst'
    OR job_title_short = 'Data Engineer'
GROUP BY 
    job_title_short,
    DATE_TRUNC('month', job_posted_date)
ORDER BY
    posted_month,
    job_title_short;


---LAG() هات قيمة الصف الي قبله
WITH monthly_job_growth AS (
    SELECT
        DATE_TRUNC('month', job_posted_date) AS posted_month,
        COUNT(*) AS total_jobs
    FROM
        job_postings_fact
    GROUP BY
        DATE_TRUNC('month', job_posted_date)
)
SELECT
    LAG(total_jobs) OVER(
        ORDER BY posted_month
    ) AS previous_month,
    total_jobs - LAG(total_jobs) over(
        ORDER BY posted_month
    ) AS job_difference,
    posted_month,
    total_jobs
FROM    
    monthly_job_growth
ORDER BY
    posted_month;


WITH 