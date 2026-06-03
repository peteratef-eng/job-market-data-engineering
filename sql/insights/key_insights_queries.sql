-- Insight 1: TOP SKILLS FOR DATA ENGINEER
SELECT
    clean_skill_name,
    clean_skill_type,
    demand_count
FROM
    mart_skill_demand_by_role
WHERE
    job_title_short = 'Data Engineer'
ORDER BY
    demand_count DESC
LIMIT 10;

-- Insight 2: REMOTE TREND FOR DATA ENGINEER
SELECT
    posted_month,
    remote_status,
    total_jobs,
    remote_status_percentage
FROM
    mart_remote_work_trends
WHERE
    job_title_short = 'Data Engineer'
    AND remote_status IN ('Remote', 'Onsite') 
ORDER BY
    posted_month,
    remote_status;
-- Insight 3: SALARY TREND FOR DATA ENGINEER
SELECT
    posted_month,
    remote_status,
    total_salary_jobs,
    avg_salary,
    previous_month_avg_salary,
    salary_difference,
    salary_growth_percentage
FROM    
    mart_salary_trends
WHERE
    job_title_short = 'Data Engineer'
    AND remote_status IN ('Remote', 'Onsite')
ORDER BY
    posted_month,
    remote_status;
-- Insight 4: TOP HIRING COMPANIES
SELECT
    clean_company_name,
    total_jobs,
    remote_jobs,
    onsite_jobs,
    remote_percentage,
    known_salary_jobs,
    avg_salary
FROM    
    mart_company_leaderboard
ORDER BY
    total_jobs DESC
LIMIT 20;
-- Insight 5: MONTHLY JOB MARKET GROWTH
SELECT
    posted_month,
    total_jobs,
    previous_month_jobs,
    job_difference,
    job_growth_percentage
FROM
    mart_monthly_job_trends
ORDER BY
    posted_month;