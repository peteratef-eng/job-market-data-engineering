SELECT
    job_title_short,
    salary_year_avg
FROM
    job_postings_fact
ORDER BY
    salary_year_avg DESC;


SELECT
    COUNT(job_id) AS total_jobs,
    job_location
FROM
    job_postings_fact
GROUP BY
    job_location
ORDER BY
    total_jobs DESC;


SELECT
    job_title,
    AVG(salary_year_avg) AS salary_avg
FROM
    job_postings_fact
GROUP BY
    job_title
HAVING 
    AVG(salary_year_avg) IS NOT NULL;



SELECT
    COUNT(job_id) AS total_jobs,
    job_title
FROM
    job_postings_fact
WHERE
    job_work_from_home = TRUE
GROUP BY
    job_title
ORDER BY
    total_jobs DESC;




SELECT
    COUNT(job_id) AS total_jobs,
    job_title
FROM
    job_postings_fact
WHERE
    job_work_from_home = TRUE
GROUP BY
    job_title
ORDER BY
    total_jobs DESC;


SELECT
    MAX(job_id) AS max_jobs
FROM
    job_postings_fact
limit 10;


SELECT
    cd.name,
    COUNT(jpf.job_id) AS total_postings
FROM
    job_postings_fact   AS jpf
INNER JOIN  company_dim AS cd
    ON  jpf.company_id = cd.company_id
GROUP BY
    cd.name
ORDER BY
    total_postings DESC
LIMIT 10;

SELECT
    job_title_short AS job_name,
    MAX(salary_year_avg) AS max_salary
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    job_title_short
ORDER BY
    max_salary DESC;


---TASK #6

SELECT
    job_title_short AS job_name,
    AVG(salary_year_avg) AS salary_avg
FROM
    job_postings_fact 
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    job_title_short
HAVING
    salary_avg > 100_000
ORDER BY
    salary_avg DESC
LIMIT
    10;

---TASK #7

SELECT
    job_title_short AS job_name,
    job_work_from_home,
    COUNT(job_id) AS total_jobs
FROM
    job_postings_fact
GROUP BY
    job_work_from_home,
    job_title_short
ORDER BY
    job_title_short ASC;

---TASK #8

SELECT
    job_location,
    COUNT(job_id) AS total_jobs
FROM
    job_postings_fact
WHERE
    job_location <> 'Anywhere' ---best to use <> than NOT LIKE*
GROUP BY
    job_location
ORDER BY
    total_jobs DESC;

---TASK #9

SELECT
    cd.name AS company_name,
    COUNT(jpf.job_id) AS total_jobs,
    AVG(jpf.salary_year_avg) AS salary_avg
FROM
    job_postings_fact AS jpf
INNER JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    jpf.salary_year_avg IS NOT NULL
GROUP BY 
    company_name
HAVING
    total_jobs >= 5
ORDER BY
    salary_avg DESC
LIMIT 10;


---TASK #10

SELECT
    cd.name AS company_name,
    COUNT(jpf.job_id) AS total_jobs,
    ROUND(MAX(jpf.salary_year_avg), 0) AS max_salary,
    ROUND(MIN(jpf.salary_year_avg), 0) AS min_salary,
    ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg
FROM 
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    company_name
ORDER BY 
    total_jobs DESC;

/*
---skills_job_dim
        skill_id │ job_id │

---company_dim
│ company_id │ name │ link_google │ thumbnail│

---skills_dim 
    │ skill_id │   skills   │    type     │
*/

SELECT *
FROM company_dim
LIMIT 5;


---TASK #11

SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count
FROM
    job_postings_fact AS jpf
JOIN    skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN    skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
GROUP BY
    sd.skills
ORDER BY
    demand_count DESC
LIMIT 
    20;


---TASK #12

SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count
FROM
    job_postings_fact AS jpf
JOIN    skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN   skills_dim  AS sd
    ON sjd.skill_id = sd.skill_id
WHERE
    jpf.job_title_short = 'Data Analyst'
GROUP BY
    sd.skills
ORDER BY demand_count DESC
LIMIT
    20;

---TASK #13

SELECT
    sd.skills AS skill_name,
    ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg
FROM
    job_postings_fact AS jpf
JOIN    skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN    skills_dim AS sd
    ON  sjd.skill_id = sd.skill_id
WHERE
    jpf.job_title_short = 'Data Analyst'
    AND jpf.salary_year_avg IS NOT NULL
GROUP BY
    sd.skills
ORDER BY
    salary_avg DESC
LIMIT
    20;

---TASK #14

SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg
FROM
    job_postings_fact AS jpf
JOIN    skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN    skills_dim AS sd
    ON  sjd.skill_id = sd.skill_id
WHERE
    jpf.job_title_short = 'Data Analyst'
    AND jpf.salary_year_avg IS NOT NULL
GROUP BY
    sd.skills
HAVING
    demand_count >= 10
ORDER BY
    salary_avg DESC
LIMIT 20;

---TASK #15

SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg
FROM
    job_postings_fact AS jpf
JOIN    skills_job_dim AS sjd
    ON  jpf.job_id = sjd.job_id
JOIN    skills_dim AS sd
    ON  sjd.skill_id = sd.skill_id
WHERE
    jpf.job_title_short = 'Data Analyst'
    AND jpf.salary_year_avg IS NOT NULL
    AND jpf.job_work_from_home = TRUE
GROUP BY
    sd.skills
HAVING
    demand_count >= 10
ORDER BY
    salary_avg DESC
LIMIT 20;



---CTEs "Common Table Expressions" Lesson* 

/*
A CTE, or Common Table Expression, lets you create a temporary named result
using WITH. You can then query that result like a table.
*/

---CTE EXAMPLE #1: Average salary by role

WITH role_salary AS (
    SELECT
        job_title_short,
        ROUND(AVG(salary_year_avg), 0) AS salary_avg
    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
    GROUP BY
        job_title_short
)
SELECT
    job_title_short,
    salary_avg
FROM
    role_salary
ORDER BY
    salary_avg DESC;


---CTE EXAMPLE #2: Remote job count by role

WITH remote_jobs AS (
    SELECT
        job_title_short,
        COUNT(job_id) AS total_remote_jobs
    FROM
        job_postings_fact
    WHERE
        job_work_from_home = TRUE
    GROUP BY
        job_title_short
)
SELECT
    job_title_short,
    total_remote_jobs
FROM
    remote_jobs
ORDER BY
    total_remote_jobs DESC;


---CTE EXAMPLE #3: Top companies by number of job postings

WITH company_job_count AS (
    SELECT
        cd.name AS company_name,
        COUNT(jpf.job_id) AS total_jobs
    FROM
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
    GROUP BY
        cd.name
)
SELECT
    company_name,
    total_jobs
FROM
    company_job_count
ORDER BY
    total_jobs DESC
LIMIT 10;


---CTE EXAMPLE #4: Most demanded skills for Data Analyst jobs

WITH data_analyst_skills AS (
    SELECT
        sd.skills AS skill_name,
        COUNT(jpf.job_id) AS demand_count
    FROM
        job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    WHERE
        jpf.job_title_short = 'Data Analyst'
    GROUP BY
        sd.skills
)
SELECT
    skill_name,
    demand_count
FROM
    data_analyst_skills
ORDER BY
    demand_count DESC
LIMIT 20;


---CTE EXAMPLE #5: High-demand, high-salary skills for remote Data Analyst jobs

WITH remote_data_analyst_skills AS (
    SELECT
        sd.skills AS skill_name,
        COUNT(jpf.job_id) AS demand_count,
        ROUND(AVG(jpf.salary_year_avg), 0) AS salary_avg
    FROM
        job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    WHERE
        jpf.job_title_short = 'Data Analyst'
        AND jpf.job_work_from_home = TRUE
        AND jpf.salary_year_avg IS NOT NULL
    GROUP BY
        sd.skills
)
SELECT
    skill_name,
    demand_count,
    salary_avg
FROM
    remote_data_analyst_skills
WHERE
    demand_count >= 10
ORDER BY
    salary_avg DESC
LIMIT 20;


/*
CTE PRACTICE QUESTIONS

Write your answers below each question. After you finish, ask me to review them.
*/

---QUESTION #1
---Use a CTE to find the top 10 job locations with the highest number of job postings.


---QUESTION #2
---Use a CTE to calculate the average yearly salary for each job_title_short.
---Return only roles where the average salary is greater than 100000.


---QUESTION #3
---Use a CTE to find the top 10 companies with the most remote job postings.


---QUESTION #4
---Use a CTE to find the top 15 most demanded skills for Data Engineer jobs.


---QUESTION #5
---Use a CTE to find skills for Data Analyst jobs where demand_count is at least 20.
---Return skill_name, demand_count, and salary_avg, ordered by salary_avg descending.








---TASK #21 CTEs TEST


/*
اعمل نفس Task 19 لكن باستخدام CTE.

اسم الـ CTE:

skill_stats

المطلوب:

skill_name
demand_count
avg_salary
score

والـ score:

avg_salary * demand_count
*/
WITH skill_stats AS (
    SELECT
        sd.skills AS skill_name,
        COUNT(DISTINCT jpf.job_id) AS total_jobs,
        ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
        COUNT(DISTINCT jpf.job_id) * ROUND(AVG(jpf.salary_year_avg), 0) AS score
    FROM
        job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    WHERE
         jpf.salary_year_avg IS NOT NULL
         AND jpf.job_title_short = 'Data Analyst'
    GROUP BY
         sd.skillS
    HAVING
         COUNT(DISTINCT jpf.job_id) >= 10
)
SELECT
    skill_name,
    total_jobs,
    avg_salary,
    score
FROM skill_stats
ORDER BY
    score DESC
LIMIT 20 ;

---tASK #22
WITH top_companies AS (
    SELECT
        cd.name AS company_name,
        COUNT(DISTINCT jpf.job_id) AS total_jobs
    FROM
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
    GROUP BY 
        cd.name
    HAVING
        COUNT(DISTINCT jpf.job_id) > 100
)
SELECT
    company_name,
    total_jobs
FROM top_companies
order by
    total_jobs DESC
limit 20;

---tASK #23

WITH remote_jobs AS (
    SELECT
        jpf.job_title_short AS job_name,
        COUNT(DISTINCT jpf.job_id) AS total_jobs,
        ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary
    FROM
        job_postings_fact AS jpf
    WHERE
        jpf.job_work_from_home = TRUE
        AND jpf.salary_year_avg IS NOT NULL
    GROUP BY
        jpf.job_title_short
)
SELECT
    job_name,
    total_jobs,
    avg_salary
FROM
    remote_jobs
ORDER BY
    total_jobs DESC
LIMIT 20;


---WINDOW FUNCTIONS
/*
FUNCTION(column) OVER(
  PARTITION BY column
  ORDER BY column
)
*/

SELECT
  job_id,
  job_title_short,
  salary_year_avg,
  AVG(salary_year_avg) OVER(PARTITION BY job_title_short) AS avg_salary_for_title
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL;

WITH salary_data AS (
    SELECT
        job_id,
        job_title_short,
        salary_year_avg,
        AVG(salary_year_avg)
        OVER(PARTITION BY job_title_short) AS avg_salary

    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)

SELECT
    *,
    salary_year_avg - avg_salary AS salary_difference
FROM salary_data;


SELECT
    job_title_short,
    salary_year_avg,
    AVG(salary_year_avg)
        OVER(PARTITION BY job_title_short) AS avg_salary
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL;


WITH ranked_jobs AS (
  SELECT
    job_id,
    job_title_short,
    salary_year_avg,
    ROW_NUMBER() OVER(
      PARTITION BY job_title_short
      ORDER BY salary_year_avg DESC
    ) AS rank_num
  FROM job_postings_fact
  WHERE salary_year_avg IS NOT NULL
)

SELECT
  job_id,
  job_title_short,
  salary_year_avg
FROM ranked_jobs
WHERE rank_num = 1;


SELECT
    students,
    class,
    score,
    AVG(score) OVER(PARTITION BY class) AS class_avg
FROM students;

ROW_NUMBER() OVER(
    PARTITION BY department
    ORDER BY salary DESC
) AS salary_rank


SELECT
    job_title_short,
    salary_year_avg,
    avg(salary_year_avg) over(PARTITION BY job_title_short) AS avg_salary_for_title
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL;

SELECT
    job_title_short,
    salary_year_avg,
    ROW_NUMBER() OVER(
        PARTITION BY job_title_short
        ORDER BY salary_year_avg DESC
    ) AS salary_rank
FROM job_postings_fact




WITH ranked_jobs AS (
    SELECT
        job_title_short,
        salary_year_avg,

        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS salary_rank
    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
FROM ranked_jobs
WHERE salary_rank <= 3;












---top 3 salary per job title

WITH top_salary AS (
    SELECT
        job_title_short,
        salary_year_avg,

        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS ranked_jobs

    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
SELECT job_title_short,
       salary_year_avg,
       ranked_jobs
FROM top_salary
WHERE ranked_jobs <= 3;



---TASK #1
WITH ranked_jobs AS (
    SELECT
        job_title_short,
        salary_year_avg,
        AVG(salary_year_avg) OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS avg_salary_for_title
    FROM job_postings_fact
)
SELECT 
    job_title_short,
    salary_year_avg,
    avg_salary_for_title
FROM average_per_group
WHERE salary_year_avg IS NOT NULL;

---TASK#2
WITH average_per_group AS (
    SELECT
        job_title_short,
        salary_year_avg,
        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS avg_salary_for_title
    FROM job_postings_fact
)
SELECT 
    job_title_short,
    salary_year_avg,
    avg_salary_for_title
FROM average_per_group
WHERE salary_year_avg IS NOT NULL;
---TASK#3
WITH ranked_jobs AS (
    SELECT
        job_title_short,
        salary_year_avg,
        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg
        ) AS top_salary
    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
SELECT
job_title_short,
salary_year_avg
FROM ranked_jobs
WHERE top_salary = 1;


/*
الخلاصة:
PARTITION BY = قسّم حسب الوظيفة.
ORDER BY salary_year_avg DESC = رتب المرتبات من الأعلى للأقل.
ROW_NUMBER() = ادي رقم لكل صف.
WHERE salary_rank = 1 = هات أعلى مرتب فقط.
*/
WITH top_five_salary AS (
    SELECT
        job_title_short,
        salary_year_avg,
        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS salary
    FROM
        job_postings_fact
    WHERE 
        salary_year_avg IS NOT NULL
)
SELECT 
    job_title_short,
    salary_year_avg,
    salary
FROM top_five_salary
WHERE salary <= 5;



---lowest salary per title

WITH salary AS (
    SELECT
        job_title_short,
        salary_year_avg,

        ROW_NUMBER() over(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg ASC
        ) AS lowest_salary

    FROM 
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
) 
SELECT
    job_title_short,
    salary_year_avg,
    lowest_salary
FROM salary
WHERE lowest_salary = 1;




WITH salary AS (
    SELECT
        job_title_short,
        salary_year_avg,

        AVG(salary_year_avg) OVER(
            PARTITION BY job_title_short
        ) AS salary_per_title,

        salary_year_avg - 
        AVG(salary_year_avg) OVER(

        ) AS salary_difference
    FROM
        job_postings_fact
    WHERE   salary_year_avg IS NOT NULL
)

SELECT
    job_title_short,
    salary_year_avg,
    salary_difference,
    salary_per_title
FROM salary;
-------------

WITH salary AS (
    SELECT
        job_title_short,
        salary_year_avg,

        AVG(salary_year_avg) OVER(
            PARTITION BY job_title_short
        ) AS salary_per_title,

        salary_year_avg - 
        AVG(salary_year_avg) OVER(
            PARTITION BY job_title_short
        ) AS salary_difference
    
    FROM
        job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
SELECT 
    job_title_short,
    salary_year_avg,
    salary_difference,
    salary_per_title

FROM salary;





--------

WITH ranked_jobs AS (
    SELECT
        job_title_short,
        salary_year_avg,

        RANK() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS rank_num

    FROM  
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)

SELECT
    job_title_short,
    salary_year_avg,
    rank_num
FROM ranked_jobs;




---DENSE_RANK() USE THIS FOR TASK #8*

WITH ranked_jobs AS (
    SELECT
        job_title_short,
        salary_year_avg,

        DENSE_RANK() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS dense_rank
    FROM 
        job_postings_fact
    WHERE 
        salary_year_avg IS NOT NULL
)

SELECT
    job_title_short,
    salary_year_avg,
    dense_rank

FROM ranked_jobs ;

---------

WITH runing_total AS (
    SELECT
        job_title_short,
        salary_year_avg,

        SUM(salary_year_avg) OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg
        ) AS total_salary

    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    total_salary

FROM runing_total;

/*
---Window Functions
ROW_NUMBER()
RANK()
DENSE_RANK()
AVG() OVER()
*/



---CASE WHEN
---EX#1
SELECT
    job_title_short,
    salary_year_avg,
    CASE
        WHEN salary_year_avg >= 150_000 THEN 'High Salary'
        WHEN salary_year_avg >= 80_000 THEN 'Medium Salary'
        ELSE 'Low Salary'
    END AS salary_category
FROM 
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL;


--------
---EX#26 CASE WHEN*

SELECT
    job_title_short,
    job_title,
    salary_year_avg,
    CASE
        WHEN salary_year_avg >= 150000 THEN 'HIGH SALARY'
        WHEN salary_year_avg BETWEEN 149999 AND 80000 THEN 'MEDIUM SALARY'
        ELSE 'LOW SALARY'
    END AS salary_category
FROM
    job_postings_fact
WHERE 
    salary_year_avg IS NOT NULL
ORDER BY salary_year_avg DESC;

---EX#26 THE SAME EXAMPLE BUT USING CTEs.

WITH salary AS (
    SELECT
        job_title_short,
        job_title,
        salary_year_avg,

        CASE
            WHEN salary_year_avg >= 150000 THEN 'High Salary'
            WHEN salary_year_avg BETWEEN 149999 AND 80000 THEN 'Medium Salary'
            ELSE 'Low Salary'
        END AS salary_category

    FROM
        job_postings_fact
    WHERE 
        salary_year_avg IS NOT NULL   
)

SELECT
    job_title_short,
    job_title,
    salary_year_avg,
    salary_category
FROM    
    salary
ORDER BY 
    salary_year_avg DESC;


---EX#27

WITH remote_type AS (
    SELECT
        job_title_short,
        COUNT(job_id) AS total_jobs,

        CASE
            WHEN job_work_from_home = TRUE THEN 'Remote'
            ELSE 'Onsite'
        END AS work_type
    FROM
        job_postings_fact
)

SELECT
    job_title_short,
    total_jobs,
    work_type
FROM    
    remote_type
GROUP BY 
    job_title_short,
    work_type
ORDER BY job_title_short ASC,
         total_jobs DESC;


WITH remote_type AS (
    SELECT
        job_title_short,

        CASE
            WHEN job_work_from_home = TRUE THEN 'Remote'
            ELSE 'Onsite'
        END AS work_type

    FROM
        job_postings_fact
)

SELECT
    job_title_short,
    work_type,
    COUNT(*) AS total_jobs
FROM    
    remote_type
GROUP BY
    job_title_short,
    work_type
ORDER BY
    job_title_short ASC,
    total_jobs DESC;


---TASK#28

WITH salary_buckets_summary AS (
    SELECT
        salary_year_avg,

        CASE
            WHEN salary_year_avg >= 150_000 THEN 'High Salary'
            WHEN salary_year_avg >= 80_000  THEN 'Medium Salary'
            ELSE 'Low Salary'
        END AS salary_category

    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)   

SELECT
    salary_category,
    count(*) AS total_jobs,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary
FROM
    salary_buckets_summary
GROUP by
    salary_category
ORDER BY avg_salary DESC;

----Cleaning NULLs + CAST + COALESCE

SELECT
    job_title_short,
    COALESCE(job_location, 'Unkown') AS clean_location
FROM job_postings_fact
WHERE
    job_location IS NULL
LIMIT 15;

SELECT
    MIN(salary_year_avg) AS min_salary,
    AVG(salary_year_avg) AS avg_salary
FROM
    job_postings_fact;



WITH cleaning_salary AS (
    SELECT
        salary_year_avg AS salary_before_clean,
        COALESCE(salary_year_avg, 15_000) AS salary_clean
    FROM    
        job_postings_fact
)
SELECT  
    salary_clean,
    salary_before_clean
FROM
    cleaning_salary
ORDER BY
    salary_before_clean NULLS FIRST;



---CAST
SELECT
    CAST(salary_year_avg AS INTEGER) AS salary_int
FROM
    job_postings_fact;


----TASK#29 Clean Locations

WITH clean_location AS (
    SELECT
        job_title_short,
        job_location,
        (
            CASE
                WHEN job_location IS NULL THEN 'Unkown'
                WHEN job_location = 'Anywhere' THEN 'Remote'
                ELSE job_location
            END 
        ) AS clean_location
    FROM    
        job_postings_fact
)
SELECT
    job_title_short,
    job_location,
    clean_location
FROM
    clean_location;

---TASK#30 SALAEY TYPE CASTING
WITH salary_type_casting AS (
    SELECT
    job_title_short,
    salary_year_avg,

    CAST(salary_year_avg AS INTEGER) AS salary_int

    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    salary_int
FROM 
    SALAEY_TYPE_CASTING
ORDER BY 
    salary_year_avg DESC;

---TASK#31 CLEAN COMPANY NAMES     
WITH clean_company_names AS (
    SELECT
    cd.name AS company_name,
    cd.company_id AS ID,
    COALESCE(cd.name, 'Unknown Company') AS clean_company_name
    FROM
        company_dim AS cd
    WHERE
        cd.company_id = 110011
)
SELECT
    company_name,
    ID,
    clean_company_name
FROM
    clean_company_names;

---I USED THIS SECOND QUERY TO KNOW IF WE HAVE 1 COMPANY ONLY WITH NO NAME
---SO YES WE HAVE 1 COMPANY WITHOUT NAME
/*
┌──────────────────────────┬────────────┐
│           name           │ company_id │
│         varchar          │   int32    │
├──────────────────────────┼────────────┤
│ AIMS International Spain │     110000 │
│ Hollard Insurance        │     110003 │
│ Carrière uitzendbureau   │     110009 │
│ CEAT                     │     110010 │
│ NULL                     │     110011 │
│ SC Johnson & Son Inc.    │     110012 │
└──────────────────────────┴────────────┘
*/
SELECT
    cd.name,
    cd.company_id
FROM 
    company_dim as cd
WHERE
    cd.company_id BETWEEN 110000 AND 110012;


SELECT
    COUNT(*) AS null_company_names
FROM
    company_dim AS cd
WHERE
    cd.name IS NULL;

---TRIM تشيل اي مسافه في الكلمه
---I USED THIS CODE TO SEE AT FIRST IF I HAVE A SPACES ON THIS DATA
SELECT
    jpf.job_location,
    jpf.job_title,
    cd.name
FROM job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    (jpf.job_location LIKE ' %' OR jpf.job_location LIKE '% ')
    OR (jpf.job_title LIKE ' %' OR jpf.job_title LIKE '% ')
    OR (cd.name LIKE ' %' OR cd.name LIKE '% ');
/*
┌──────────────────────────────┬──────────────────────────────┬───────────────────────────────┐
│         job_location         │          job_title           │             name              │
│           varchar            │           varchar            │            varchar            │
├──────────────────────────────┼──────────────────────────────┼───────────────────────────────┤
│ Austin, TX                   │ Data Engineer                │ Diverse Lynx                  │
│ Plano, TX                    │ Data Engineer                │ Trident Consulting            │
│ Irving, TX                   │  Splunk Business Analyst     │ Resource Informatics Group, … │
│ Alpharetta, GA               │ Senior Data Scientist        │ Trident Consulting            │
│ Dallas, TX                   │ Snowflake Data Engineer      │ VLink Inc                     │
│ Belarus                      │ Data scientist               │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Reston, VA                   │  Data and Reporting Analyst  │ RIT Solutions, Inc.           │
│ Dallas, TX                   │ Data Architect with Data En… │ Resource Logistics Inc.       │
│ Atlanta, GA                  │ Data Scientist               │ MindSource                    │
│ Belarus                      │ Data Engineer                │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Belarus                      │ Data Engineer                │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Fremont, CA                  │ Data Engineer with QE exper… │ Info Way Solutions            │
│ Fremont, CA                  │ Data Engineer                │ Info Way Solutions            │
│ Washington, DC               │  GenAI Data Scientist        │ RIT Solutions, Inc.           │
│ United States                │ Big Data Engineer            │ RIT Solutions, Inc.           │
│ Richardson, TX               │  GCP Data Engineer           │ Cybertec, Inc                 │
│ Fremont, CA                  │ Data Engineer                │ Info Way Solutions            │
│ Austin, TX                   │ Data Analyst                 │ Rapid Consulting Services     │
│ Wayzata, MN                  │  Celonis Data Engineer       │ RIT Solutions, Inc.           │
│ Fremont, CA                  │ Senior Data Analyst          │ Info Way Solutions            │
│ Fremont, CA                  │ Role: Data Engineer          │ Info Way Solutions            │
│ Austin, TX                   │ Data Engineer Spark + Scala  │ VLink Inc                     │
│ Belarus                      │ Cloud data scientist         │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Belarus                      │ Data Engineer                │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Belarus                      │ Digital Marketer             │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Belarus                      │ Big Data Engineer            │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Belarus                      │ Middle Java Software Engine… │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Dubai - United Arab Emirates │ Data Scientist               │ Emirates Transport            │
│ Paris, France                │ Mission Data Engineer H/F  … │ Rheso.Tech 🔎 Recrutement & … │
│ Indianapolis, IN             │ Data Engineer                │ Pinnacle Partners, Inc        │
│ Belarus                      │ Data scientist               │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ United Kingdom               │ Lead Engineer - Kubernetes … │ Couchbase, Inc.               │
│ Tel Aviv-Yafo, Israel        │ Technical Support Engineer … │ Couchbase, Inc.               │
│ Seoul, South Korea           │  Staff, Data Scientist (SCM) │ Coupang                       │
│ Belarus                      │ Big Data Engineer            │ Ð Ð´Ð¼Ð¸Ð½Ð¸Ñ Ñ Ñ Ð°Ñ Ð¸Ð²Ð½… │
│ Anywhere                     │ Machine Learning Engineer    │ Sky Systems, Inc. (SkySys)    │
└──────────────────────────────┴──────────────────────────────┴───────────────────────────────┘
*/
---AND I WILL USE TRIM TO FIX IT 
WITH clean_company_names AS (
    SELECT
        TRIM(cd.name) AS clean_company_name,
        TRIM(jpf.job_title) AS clean_title_name,
        TRIM(jpf.job_location) AS clean_location_name
    FROM
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
)
SELECT
    clean_company_name,
    clean_title_name,
    clean_location_name
FROM
    clean_company_names;

/*
THE RESULT OF THIS QUERY IS :
┌────────────────────────────────┬───────────────────────────────┬────────────────────────────┐
│       clean_company_name       │       clean_title_name        │    clean_location_name     │
│            varchar             │            varchar            │          varchar           │
├────────────────────────────────┼───────────────────────────────┼────────────────────────────┤
│ Metasys Technologies           │ Data Analyst                  │ New York, NY               │
│ Guidehouse                     │ Data Analyst                  │ Washington, DC             │
│ Protask                        │ Data Analyst                  │ Fairfax, VA                │
│ Atria Wealth Solutions         │ Senior Data Analyst / Platfo… │ Worcester, MA              │
│ ICONMA, LLC                    │ Data Analyst                  │ Sunnyvale, CA              │
│ Aquent                         │ Jr. Data Analyst              │ Torrance, CA               │
│ Adyen                          │ Data Analyst                  │ San Francisco, CA          │
│ Albertsons Companies           │ Loyalty Data Analyst III      │ Pleasanton, CA             │
│ Panda Restaurant Group         │ Senior data analyst           │ Rosemead, CA               │
│ Diverse Lynx                   │ Business Analyst - Taxonomy/… │ Thousand Oaks, CA          │
│ Range Generation Next LLC      │ Technical Data Analyst / Des… │ Vandenberg AFB, CA         │
│ Stanford University Lee Lab    │ Neuroscience Research Data A… │ Stanford, CA               │
│ CYNET SYSTEMS                  │ Data Analyst                  │ Irvine, CA                 │
│ Trident Consulting             │ BI Data Analyst               │ San Jose, CA               │
│ EDI Staffing                   │ EDI Data Analyst              │ Fullerton, CA              │
│ Workway                        │ Data Analyst for Member Cont… │ Pasadena, CA               │
│ Omega Solutions                │ BI Data Analyst               │ Santa Clara, CA            │
│ ByteDance                      │ Data Analyst, Partner Operat… │ San Francisco, CA          │
│ Tekfortune Inc.                │ Guidewire Policy Data Analyst │ Sunnyvale, CA              │
│ VLink Inc.                     │ Sr. Data Analyst              │ Los Angeles, CA            │
│     ·                          │        ·                      │    ·                       │
│     ·                          │        ·                      │    ·                       │
│     ·                          │        ·                      │    ·                       │
│ Apex Systems                   │ Sr. Data Engineer             │ Anywhere                   │
│ Delta Dental of Washington     │ Data Quality Assurance Engin… │ Spokane, WA                │
│ Tata Consultancy Services      │ Data Engineer- Python, Snowf… │ Sunnyvale, CA              │
│ Motion Recruitment             │ AI/ML Data Engineer           │ Anywhere                   │
│ Alt                            │ Senior Data Engineer          │ Anywhere                   │
│ SightSpectrum                  │ Data Engineer - H1B, H4. USC… │ Elkridge, MD               │
│ Agile Tech Labs                │ Senior Data Engineer          │ Detroit, MI                │
│ HatchPros                      │ Azure Data Engineer           │ Jersey City, NJ            │
│ Envision Technology Solutions  │ Data Engineer                 │ McLean, VA                 │
│ Menhir Financial               │ ML Engineer                   │ Anywhere                   │
│ NEORIS                         │ Data Scientist                │ Peru                       │
│ T D Newton                     │ Data Scientist - Machine Lea… │ Mumbai, Maharashtra, India │
│ Cedeo                          │ STAGE - Assistant(e) Data An… │ Tremblay-en-France, France │
│ Free-Work (ex Freelance-info … │ Data Scientist NLP - Secteur… │ Paris, France              │
│ CVM Data Sciences              │ SQL-Focused Data Scientist    │ Toronto, ON, Canada        │
│ Limitless Staffing             │ Machine Learning Engineer     │ Toronto, ON, Canada        │
│ Hopper                         │ Senior Machine Learning Engi… │ Anywhere                   │
│ Jooble                         │ Data Scientist                │ London, United Kingdom     │
│ Jooble                         │ Senior Data Scientist         │ London, United Kingdom     │
│ Ashdown Group                  │ Cloud Data Engineer           │ Surbiton, UK               │
└────────────────────────────────┴───────────────────────────────┴────────────────────────────┘
*/


SELECT
    jpf.job_title AS original_job_title,
    TRIM(jpf.job_title) AS clean_title_name,
    cd.name AS original_company_name,
    TRIM(cd.name) AS clean_company_name,
    jpf.job_location AS original_location_name,
    TRIM(jpf.job_location) AS clean_location_name
FROM   
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id

WHERE
    (jpf.job_title LIKE ' %' OR jpf.job_title LIKE '% ')
    OR (cd.name LIKE ' %' OR cd.name LIKE '% ')
    OR (jpf.job_location LIKE ' %' OR jpf.job_location LIKE '% ');



SELECT
    jpf.job_title AS original_job_title,
    TRIM(jpf.job_title) AS clean_title_name,
    cd.name AS original_company_name,
    TRIM(cd.name) AS clean_company_name,
    jpf.job_location AS original_location_name,
    TRIM(jpf.job_location) AS clean_location_name,
    CASE WHEN jpf.job_title LIKE ' %' OR jpf.job_title LIKE '% ' 
         OR cd.name LIKE ' %' OR cd.name LIKE '% '
         OR jpf.job_location LIKE ' %' OR jpf.job_location LIKE '% '
         THEN 'Has Spaces'
         ELSE 'Clean' 
    END AS space_status
FROM job_postings_fact AS jpf
JOIN company_dim AS cd ON jpf.company_id = cd.company_id
WHERE
    jpf.job_title LIKE ' %' OR jpf.job_title LIKE '% ' ;



WITH cleaned_jobs AS (
    SELECT
        jpf.job_id,
        TRIM(jpf.job_title) AS clean_job_title,
        TRIM(jpf.job_title_short) AS clean_job_title_short,
        TRIM(jpf.job_location) AS clean_job_location,
        TRIM(cd.name) AS clean_company_name
    FROM
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
)
SELECT
    *
FROM
    cleaned_jobs;


SELECT
    LOWER(jpf.job_title_short) job_name,
    UPPER(cd.name) company_name
FROM    
    job_postings_fact jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
LIMIT 20;


SELECT
    COALESCE(NULLIF(job_title_short, 'Data Analyst'), 'ANALYST :D') AS modified_title
FROM
    job_postings_fact;

---Data Quality Checks

SELECT
    COUNT(*) AS total_rows,
    COUNT(job_id) AS jobs_with_id,
    COUNT(salary_year_avg) AS salary_rows_number,
    COUNT(*) - COUNT(salary_year_avg) AS missing_salary_count
FROM 
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL;

SELECT
    COUNT(*) AS total_rows,
    COUNT(cd.company_id) AS ID,
    COUNT(*) - COUNT(cd.name) AS missing_companies
FROM 
    company_dim AS cd;


SELECT
    jpf.job_title_short,
    jpf.salary_year_avg,
    jpf.job_location,
    cd.name,
    cd.company_id
FROM
    company_dim AS cd
LEFT JOIN job_postings_fact AS jpf
    ON cd.company_id = jpf.company_id
WHERE 
    cd.company_id = 215940;


SELECT
    company_id,
    name
FROM
    company_dim
WHERE
    company_id = 215940;





SELECT
    company_id,
    name,
    link_google,
    thumbnail
FROM
    company_dim
WHERE
    company_id = 215940;

SELECT
    COUNT(*) AS total_jobs
FROM
    job_postings_fact
WHERE
    company_id = 215940;


SELECT
    COUNT(*) AS jobs_with_this_company_id
FROM
    job_postings_fact
WHERE
    company_id = 215940;



SELECT
    jpf.company_id,
    COUNT(*) AS total_jobs
FROM
    job_postings_fact AS jpf
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    cd.company_id IS NULL
GROUP BY
    jpf.company_id
ORDER BY
    total_jobs DESC;




SELECT
    COUNT(*) AS total_jobs,
    COUNT(cd.company_id) AS jobs_with_valid_company,
    COUNT(*) - COUNT(cd.company_id) AS jobs_with_missing_company_reference
FROM
    job_postings_fact AS jpf
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id;



---Duplicate Checks

SELECT
    cd.company_id,
    COUNT(*) AS total_jobs,
    cd.name
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
Group by 
    cd.company_id,
    cd.name
HAVING
    COUNT(*) > 1
ORDER BY 
    total_jobs;



SELECT
    job_title_short,
    salary_year_avg,
    job_location
FROM
    job_postings_fact AS jpf
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    cd.company_id = 1366385;


SELECT
    jpf.job_id,
    jpf.job_title_short,
    jpf.job_title,
    jpf.job_location,
    jpf.salary_year_avg
FROM
    job_postings_fact AS jpf
WHERE
    jpf.company_id = 1366385
ORDER BY
    jpf.job_title_short,
    jpf.job_location;


SELECT
    job_id,
    COUNT(*) AS duplicate_count
FROM
    job_postings_fact
GROUP BY
    job_id
HAVING
    COUNT(*) > 1;



SELECT
    company_id,
    job_title_short,
    job_title,
    job_location,
    salary_year_avg,
    COUNT(*) AS duplicate_count
FROM
    job_postings_fact
GROUP BY
    company_id,
    job_title_short,
    job_title,
    job_location,
    salary_year_avg
HAVING
    COUNT(*) > 1
ORDER BY
    duplicate_count DESC;


SELECT
    job_title,
    job_title_short,
    job_id,
    cd.company_id,
    cd.name
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    jpf.company_id = 6181;




SELECT
    COUNT(*) AS total_rows,
    COUNT(*) - COUNT(salary_year_avg) AS missing_salary_count,
    COUNT(*) - COUNT(job_location) AS missing_location_count,
    COUNT(*) - COUNT(company_id) AS missing_company_id_count
FROM
    job_postings_fact;


SELECT
    COUNT(*) AS duplicate_count,
    job_id
FROM
    job_postings_fact
GROUP BY    
    job_id
HAVING 
    duplicate_count > 1;

SELECT
    company_id,
    name,
    LOWER(TRIM(COALESCE(name, 'Unknown Company'))) AS clean_company_name
FROM
    company_dim;

DESCRIBE job_postings_fact;



SELECT
    jpf.job_title_short,
    cd.name,
    jpf.job_id,
    cd.company_id
FROM    
    job_postings_fact AS jpf
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    cd.company_id = 215940;


SELECT
    name,
    COALESCE(name, 'ANDREW'),
    NULLIF(name, 'Google')
FROM
    company_dim
    ;



WITH month

---COALESCE لو في نتيجة NULL وعايزين نحطلها قيمه
SELECT
    COALESCE(name, 'PETER') AS clean_company_name
FROM
    company_dim
WHERE
    name IS NULL;

---TRIM لو عايزين نوحد المسافات من بدايه ونهايه الكلمه
SELECT
    job_title,
    TRIM(job_title) AS clean_job_title
FROM
    job_postings_fact;

---LOWER(), UPPER() توحيد شكل الحروف كابتل او سمول
SELECT
    name,
    LOWER(name) AS small_letters,
    UPPER(name) AS capital_letters
FROM
    company_dim;

---CASE
SELECT
    ROUND(salary_year_avg),
        CASE
            WHEN salary_year_avg >= 150_000 THEN 'High Salary'
            WHEN salary_year_avg >= 80_000 THEN 'Medium Salary'
            ELSE 'Low Salary'
        END AS salary_category
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL;

---NULLIF بتحول قيمة معينة ل NULL
SELECT
    NULLIF(job_location, '') clean_location
FROM
    job_postings_fact;

SELECT
    job_location
FROM
    job_postings_fact
WHERE
    job_location = '';



SELECT
    COALESCE(NULLIF(TRIM(job_location), ''), 'Unknown') AS clean_job_location
FROM
    job_postings_fact;

---LAG() بتجيب قيمة الصف السابق

WITH monthly_jobs AS (
    SELECT
        DATE_TRUNC('day', job_posted_date) AS posted_month,
        COUNT(*) AS total_jobs
    FROM
        job_postings_fact
    GROUP BY    
        DATE_TRUNC('day', job_posted_date)
)
SELECT
    posted_month,
    total_jobs,
    LAG(total_jobs) OVER(
        ORDER BY posted_month
    ) AS previous_month_jobs
FROM
    monthly_jobs;



---TASK#1
SELECT
    job_title,
    TRIM(LOWER(job_title)) AS clean_job_title
FROM
    job_postings_fact;


---TASK#2
SELECT
    job_location,
    CASE
    WHEN COALESCE(job_location, 'Unknown')
    WHEN job_location 'Anywhere' THEN 'Remote'
    ELSE job_location
    END AS
FROM
    job_postings_fact;

SELECT
SELECT
SELECT