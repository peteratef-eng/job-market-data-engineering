/*
SQL REVIEW QUESTIONS

Write your answers under each question.
Use the same tables you practiced with:
- job_postings_fact
- company_dim
- skills_job_dim
- skills_dim
*/

/*
REVIEW NOTES AND CORRECTIONS

Overall:
- Your SQL is solid. Most answers are correct.
- Main recurring issues:
  1. Match requested output column names exactly.
  2. Match requested output column order exactly.
  3. Add ORDER BY when the question asks for ordered output.
  4. Add LIMIT when the question asks for top N.
  5. Avoid relying on SELECT aliases inside HAVING or window ORDER BY if you want portable SQL.
  6. For window-function filtering, calculate the rank in a CTE, then filter in the outer query.

Good / basically correct:
- Questions #1, #3, #5, #7, #8, #9, #10, #11, #12, #13, #14, #15,
  #17, #18, #19, #20, #22, #27, #28, #29, #30, #31, #32, #33, #34,
  #36, and #38 are basically correct.

Small notes:
- MAX(), AVG(), and MIN() ignore NULL values, so WHERE salary_year_avg IS NOT NULL
  is not always required for those aggregate calculations, but it is still okay.
- Safer HAVING style:

  HAVING AVG(salary_year_avg) > 100000

  instead of:

  HAVING avg_salary > 100000

QUESTION #2:
- Mostly correct.
- If "top jobs" means top salary, exclude NULL salary values.

Correct version:
SELECT
    job_id,
    job_title_short,
    job_title,
    job_location,
    salary_year_avg
FROM job_postings_fact
WHERE job_location = 'Anywhere'
  AND salary_year_avg IS NOT NULL
ORDER BY salary_year_avg DESC
LIMIT 20;

QUESTION #4:
- Correct logic.
- Requested output order is job_location, total_jobs.

Correct version:
SELECT
    job_location,
    COUNT(*) AS total_jobs
FROM job_postings_fact
GROUP BY job_location
ORDER BY total_jobs DESC;

SECOND QUESTION #4:
- This question should be renumbered because there are two Question #4 labels.
- Your answer is good, but job_name is extra and not needed.

Correct version:
SELECT
    cd.name AS company_name,
    COUNT(*) AS total_jobs,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary
FROM job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE jpf.job_location = 'Egypt'
  AND jpf.job_title_short = 'Data Engineer'
  AND jpf.salary_year_avg IS NOT NULL
GROUP BY cd.name
ORDER BY avg_salary DESC;

QUESTION #16:
- Correct logic.
- Requested output order is job_title_short, total_remote_jobs.

Correct version:
WITH calculate_remote AS (
    SELECT
        job_title_short,
        COUNT(*) AS total_remote_jobs
    FROM job_postings_fact
    WHERE job_work_from_home = TRUE
    GROUP BY job_title_short
)
SELECT
    job_title_short,
    total_remote_jobs
FROM calculate_remote
ORDER BY total_remote_jobs DESC;

QUESTION #21:
- Good answer.
- Use a clearer alias and add final ordering.

Correct version:
WITH top_salaries AS (
    SELECT
        job_title_short,
        salary_year_avg,
        ROW_NUMBER() OVER (
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS salary_rank
    FROM job_postings_fact
    WHERE salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    salary_rank
FROM top_salaries
WHERE salary_rank <= 3
ORDER BY job_title_short, salary_rank;

QUESTION #23:
- Logic is right.
- Requested alias is rank_num.
- Also order within each job title.

Correct version:
SELECT
    job_title_short,
    salary_year_avg,
    RANK() OVER (
        PARTITION BY job_title_short
        ORDER BY salary_year_avg DESC
    ) AS rank_num
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL
ORDER BY job_title_short, rank_num;

QUESTION #24:
- Logic is right.
- Requested alias is dense_rank.

Correct version:
SELECT
    job_title_short,
    salary_year_avg,
    DENSE_RANK() OVER (
        PARTITION BY job_title_short
        ORDER BY salary_year_avg DESC
    ) AS dense_rank
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL
ORDER BY job_title_short, dense_rank;

QUESTION #25:
- Your answer works, but duplicate salary values can get the same running total
  because the default window frame is often RANGE.
- Use ROWS for a row-by-row running total.

Correct version:
SELECT
    job_title_short,
    salary_year_avg,
    SUM(salary_year_avg) OVER (
        PARTITION BY job_title_short
        ORDER BY salary_year_avg
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_salary_total
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL
ORDER BY job_title_short, salary_year_avg;

QUESTION #26:
- Incomplete.
- Missing total overall jobs.
- Missing final ORDER BY.

Correct version:
SELECT
    job_title_short,
    COUNT(*) AS total_jobs_by_title,
    SUM(COUNT(*)) OVER () AS total_jobs,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS job_title_percentage
FROM job_postings_fact
GROUP BY job_title_short
ORDER BY job_title_percentage DESC;

QUESTION #35:
- Remove the salary filter.
- Duplicate postings can still have NULL salary_year_avg.

Correct version:
SELECT
    company_id,
    job_title_short,
    job_title,
    job_location,
    salary_year_avg,
    COUNT(*) AS duplicate_count
FROM job_postings_fact
GROUP BY
    company_id,
    job_title_short,
    job_title,
    job_location,
    salary_year_avg
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

QUESTION #37:
- Missing ORDER BY.
- Alias has typo: tOtal_jobs should be total_jobs.
- Requested output order is posted_day, total_jobs.

Correct version:
SELECT
    DATE_TRUNC('day', job_posted_date) AS posted_day,
    COUNT(*) AS total_jobs
FROM job_postings_fact
GROUP BY posted_day
ORDER BY posted_day;

QUESTION #39:
- Missing LIMIT 10.
- Alias has typo: remote_percantage should be remote_percentage.

Correct version:
SELECT
    job_title_short,
    COUNT(*) AS total_jobs,
    SUM(CASE WHEN job_work_from_home = TRUE THEN 1 ELSE 0 END) AS remote_jobs,
    ROUND(
        SUM(CASE WHEN job_work_from_home = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS remote_percentage
FROM job_postings_fact
GROUP BY job_title_short
ORDER BY remote_percentage DESC
LIMIT 10;

QUESTION #40:
- Incomplete.
- You calculated the ranks but did not filter to the highest skill per title.
- Also safer to calculate demand_count first, then apply ROW_NUMBER() in a second CTE.

Correct version:
WITH skill_demand AS (
    SELECT
        jpf.job_title_short,
        sd.skills AS skill_name,
        COUNT(*) AS demand_count
    FROM job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    GROUP BY
        jpf.job_title_short,
        sd.skills
),
ranked_skills AS (
    SELECT
        job_title_short,
        skill_name,
        demand_count,
        ROW_NUMBER() OVER (
            PARTITION BY job_title_short
            ORDER BY demand_count DESC
        ) AS skill_rank
    FROM skill_demand
)
SELECT
    job_title_short,
    skill_name,
    demand_count,
    skill_rank
FROM ranked_skills
WHERE skill_rank = 1
ORDER BY job_title_short;

INTERVIEW / PRACTICE TIPS:
- Read the requested output columns like a checklist: exact names, exact order, exact filters.
- WHERE filters raw rows before grouping.
- HAVING filters grouped/aggregated results after GROUP BY.
- Always add final ORDER BY if the question asks for ordered results.
- For top N questions, remember LIMIT.
- For window functions, do the window calculation in a CTE, then filter in the outer query.
- ROW_NUMBER() gives one row even if tied.
- RANK() keeps ties but skips numbers.
- DENSE_RANK() keeps ties without gaps.
*/


--- SECTION 1: BASIC SELECT, WHERE, ORDER BY

---QUESTION #1
---Return job_title_short and salary_year_avg from job_postings_fact.
---Only include rows where salary_year_avg is not null.
---Order by salary_year_avg from highest to lowest.
SELECT
    job_title_short,
    salary_year_avg
FROM 
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
ORDER BY
    salary_year_avg DESC;
/*
┌───────────────────────────┬─────────────────┐
│      job_title_short      │ salary_year_avg │
│          varchar          │     double      │
├───────────────────────────┼─────────────────┤
│ Data Scientist            │        960000.0 │
│ Data Scientist            │        920000.0 │
│ Senior Data Scientist     │        890000.0 │
│ Machine Learning Engineer │        875000.0 │
│ Data Scientist            │        870000.0 │
│ Data Scientist            │        850000.0 │
│ Machine Learning Engineer │        800000.0 │
│ Senior Data Engineer      │        800000.0 │
│ Data Scientist            │        680000.0 │
│ Data Analyst              │        650000.0 │
│ Data Scientist            │        640000.0 │
│ Data Engineer             │        640000.0 │
│ Data Scientist            │        585000.0 │
│ Data Scientist            │        550000.0 │
│ Data Scientist            │        525000.0 │
│ Data Engineer             │        525000.0 │
│ Data Scientist            │        475000.0 │
│ Senior Data Scientist     │        475000.0 │
│ Senior Data Scientist     │        463500.0 │
│ Data Scientist            │        450000.0 │
│       ·                   │            ·    │
│       ·                   │            ·    │
│       ·                   │            ·    │
│ Software Engineer         │         22000.0 │
│ Machine Learning Engineer │         22000.0 │
│ Software Engineer         │         21880.0 │
│ Business Analyst          │         21750.0 │
│ Data Analyst              │         21000.0 │
│ Data Analyst              │         21000.0 │
│ Data Scientist            │         20100.5 │
│ Data Scientist            │         20100.5 │
│ Data Engineer             │         20000.0 │
│ Data Analyst              │         20000.0 │
│ Cloud Engineer            │         19200.0 │
│ Data Analyst              │         19000.0 │
│ Data Analyst              │         18000.0 │
│ Data Engineer             │         18000.0 │
│ Data Scientist            │         17772.0 │
│ Data Scientist            │         16800.0 │
│ Business Analyst          │         16500.0 │
│ Data Engineer             │         15000.0 │
│ Cloud Engineer            │         15000.0 │
│ Data Engineer             │         15000.0 │
└───────────────────────────┴─────────────────┘
*/

---QUESTION #2
---Return the top 20 jobs where job_location is 'Anywhere'.
---Include job_id, job_title_short, job_title, job_location, and salary_year_avg.
SELECT
    job_title_short,
    job_id,
    job_title,
    job_location,
    salary_year_avg
FROM
    job_postings_fact
WHERE
    job_location = 'Anywhere'
ORDER BY
    salary_year_avg DESC
LIMIT 20;
/*
┌───────────────────────┬─────────┬────────────────────────────────────────────────────────────┬──────────────┬─────────────────┐
│    job_title_short    │ job_id  │                         job_title                          │ job_location │ salary_year_avg │
│        varchar        │  int32  │                          varchar                           │   varchar    │     double      │
├───────────────────────┼─────────┼────────────────────────────────────────────────────────────┼──────────────┼─────────────────┤
│ Data Scientist        │ 1574285 │ Data Scientist , Games [Remote]                            │ Anywhere     │        680000.0 │
│ Data Analyst          │  142665 │ Data Analyst                                               │ Anywhere     │        650000.0 │
│ Data Scientist        │  499552 │ Staff Data Scientist/Quant Researcher                      │ Anywhere     │        550000.0 │
│ Data Scientist        │  543480 │ Staff Data Scientist - Business Analytics                  │ Anywhere     │        525000.0 │
│ Senior Data Scientist │   95558 │ Senior Data Scientist                                      │ Anywhere     │        475000.0 │
│ Data Analyst          │ 1283788 │ Analytics Engineer (L5) - Live Quality of Experience       │ Anywhere     │        445000.0 │
│ Senior Data Scientist │  920876 │ Senior Data Scientist                                      │ Anywhere     │        445000.0 │
│ Data Engineer         │ 1231335 │ Data Engineer (L5) - Content Production & Promotion        │ Anywhere     │        445000.0 │
│ Data Engineer         │ 1241978 │ Data Engineer (L5) - Growth Insights and Foundations       │ Anywhere     │        445000.0 │
│ Data Analyst          │ 1241985 │ Analytics Engineer (L5) - Live Quality of Experience       │ Anywhere     │        445000.0 │
│ Data Scientist        │ 1558080 │ Data Scientist (L5) - Netflix Preview Club                 │ Anywhere     │        445000.0 │
│ Data Engineer         │ 1578513 │ Data Engineer - Commerce Product Data Engineering [Remote] │ Anywhere     │        445000.0 │
│ Data Analyst          │ 1598650 │ Analytics Engineer - Playback Data (L5)                    │ Anywhere     │        445000.0 │
│ Data Engineer         │ 1610938 │ Data Engineer - Content Production & Promotion [Remote]    │ Anywhere     │        445000.0 │
│ Data Analyst          │ 1009426 │ Financial & Data Analyst - Pricing (12 months Contract)    │ Anywhere     │        385000.0 │
│ Data Engineer         │ 1515084 │ VP, Engineering, Data & AI                                 │ Anywhere     │        377500.0 │
│ Data Scientist        │  464699 │ Data Scientist                                             │ Anywhere     │        375000.0 │
│ Senior Data Scientist │  535819 │ Senior Data Scientist                                      │ Anywhere     │        375000.0 │
│ Data Engineer         │ 1270532 │ Trading Data Engineer                                      │ Anywhere     │        375000.0 │
│ Data Engineer         │ 1273376 │ Trading Data Engineer                                      │ Anywhere     │        375000.0 │
└───────────────────────┴─────────┴────────────────────────────────────────────────────────────┴──────────────┴─────────────────┘
*/

---QUESTION #3
---Find the highest salary_year_avg in the job_postings_fact table.
---Return it as max_salary.
SELECT
    ROUND(MAX(salary_year_avg), 0) AS max_salary
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL;
/*
┌────────────┐
│ max_salary │
│   double   │
├────────────┤
│   960000.0 │
└────────────┘
*/

--- SECTION 2: GROUP BY, COUNT, AVG, HAVING

---QUESTION #4
---Count the number of jobs for each job_location.
---Return job_location and total_jobs.
---Order by total_jobs descending.
SELECT
    COUNT(job_id) AS total_jobs,
    job_location
FROM
    job_postings_fact
GROUP BY
    job_location
ORDER BY
    total_jobs DESC;
/*
┌────────────┬───────────────────────────────────────────────────────┐
│ total_jobs │                     job_location                      │
│   int64    │                        varchar                        │
├────────────┼───────────────────────────────────────────────────────┤
│     144668 │ Anywhere                                              │
│      38724 │ Singapore                                             │
│      20327 │ New York, NY                                          │
│      20194 │ Paris, France                                         │
│      19620 │ Bengaluru, Karnataka, India                           │
│      17319 │ United Kingdom                                        │
│      17269 │ Madrid, Spain                                         │
│      16624 │ India                                                 │
│      15482 │ London, UK                                            │
│      14932 │ Hyderabad, Telangana, India                           │
│      13968 │ Dublin, Ireland                                       │
│      13624 │ Atlanta, GA                                           │
│      12978 │ Lisbon, Portugal                                      │
│      12692 │ Hong Kong                                             │
│      12601 │ Chicago, IL                                           │
│      11535 │ United States                                         │
│      11244 │ Canada                                                │
│      10115 │ Amsterdam, Netherlands                                │
│       9974 │ Austin, TX                                            │
│       9939 │ France                                                │
│          · │   ·                                                   │
│          · │   ·                                                   │
│          · │   ·                                                   │
│          1 │ Wimpassing im Schwarzatale, Austria                   │
│          1 │ Schöneck, Germany                                     │
│          1 │ Nowy Sącz, Poland                                     │
│          1 │ Dettenhausen, Germany                                 │
│          1 │ Hampton Heath, United Kingdom                         │
│          1 │ Nantes-en-Ratier, France                              │
│          1 │ Carryduff, Belfast, UK                                │
│          1 │ Beernem, Belgium                                      │
│          1 │ Bertrange, France                                     │
│          1 │ Paray-Vieille-Poste, France                           │
│          1 │ Siavonga, Zambia                                      │
│          1 │ Perlis, Malaysia                                      │
│          1 │ Botteghino di Sesso, Province of Reggio Emilia, Italy │
│          1 │ Bargteheide, Germany                                  │
│          1 │ Houck, AZ                                             │
│          1 │ Davenport, IA   (+72 others)                          │
│          1 │ Memmingerberg, Germany                                │
│          1 │ Manchester, United Kingdom (+3 others)                │
│          1 │ Hampton Bays, NY                                      │
│          1 │ Inman, SC                                             │
└────────────┴───────────────────────────────────────────────────────┘
*/

-- Question #4
-- For Data Engineer jobs located in Egypt,
-- return each company name,
-- the total number of jobs,
-- and the average salary.
-- Only include jobs where salary_year_avg is not null.
SELECT
    cd.name AS company_name,
    jpf.job_title_short AS job_name,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
    COUNT(jpf.job_id) AS total_jobs
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    jpf.job_location = 'Egypt'
    AND salary_year_avg IS NOT NULL
    AND job_title_short = 'Data Engineer'
GROUP BY 
    cd.name,
    jpf.job_title_short
ORDER BY
    avg_salary DESC;
/*
┌──────────────────┬───────────────┬────────────┬────────────┐
│   company_name   │   job_name    │ avg_salary │ total_jobs │
│     varchar      │    varchar    │   double   │   int64    │
├──────────────────┼───────────────┼────────────┼────────────┤
│ McLedger         │ Data Engineer │   160000.0 │          1 │
│ Klivvr           │ Data Engineer │    97167.0 │          3 │
│ Nawy Real Estate │ Data Engineer │    96773.0 │          1 │
│ IBM              │ Data Engineer │    92283.0 │          1 │
│ Jumia            │ Data Engineer │    91000.0 │          1 │
│ Vodafone         │ Data Engineer │    91000.0 │          1 │
│ Mashreq          │ Data Engineer │    72800.0 │          3 │
└──────────────────┴───────────────┴────────────┴────────────┘
*/

---QUESTION #5
---Calculate the average salary for each job_title_short.
---Only include rows where salary_year_avg is not null.
---Return job_title_short and avg_salary.
---Order by avg_salary descending.
SELECT
    job_title_short,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    job_title_short
ORDER BY 
    avg_salary DESC;
/*
┌───────────────────────────┬────────────┐
│      job_title_short      │ avg_salary │
│          varchar          │   double   │
├───────────────────────────┼────────────┤
│ Senior Data Scientist     │   156391.0 │
│ Senior Data Engineer      │   149222.0 │
│ Software Engineer         │   141513.0 │
│ Machine Learning Engineer │   137332.0 │
│ Data Engineer             │   134867.0 │
│ Data Scientist            │   134324.0 │
│ Cloud Engineer            │   122464.0 │
│ Senior Data Analyst       │   115800.0 │
│ Business Analyst          │    98660.0 │
│ Data Analyst              │    93223.0 │
└───────────────────────────┴────────────┘
*/

---QUESTION #6
---Find job_title_short roles where the average salary is greater than 100000.
---Return job_title_short and avg_salary.
---Order by avg_salary descending.
SELECT
    job_title_short,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
GROUP BY
    job_title_short
HAVING 
    avg_salary > 100_000
ORDER BY
    avg_salary DESC;
/*
┌───────────────────────────┬────────────┐
│      job_title_short      │ avg_salary │
│          varchar          │   double   │
├───────────────────────────┼────────────┤
│ Senior Data Scientist     │   156391.0 │
│ Senior Data Engineer      │   149222.0 │
│ Software Engineer         │   141513.0 │
│ Machine Learning Engineer │   137332.0 │
│ Data Engineer             │   134867.0 │
│ Data Scientist            │   134324.0 │
│ Cloud Engineer            │   122464.0 │
│ Senior Data Analyst       │   115800.0 │
└───────────────────────────┴────────────┘
*/

---QUESTION #7
---Count total jobs by job_title_short and job_work_from_home.
---Return job_title_short, job_work_from_home, and total_jobs.
---Order by job_title_short.
SELECT
    job_title_short,
    job_work_from_home,
    COUNT(job_id) AS total_jobs
FROM
    job_postings_fact
GROUP BY
    job_title_short,
    job_work_from_home
ORDER BY
    job_title_short;
/*
┌───────────────────────────┬────────────────────┬────────────┐
│      job_title_short      │ job_work_from_home │ total_jobs │
│          varchar          │      boolean       │   int64    │
├───────────────────────────┼────────────────────┼────────────┤
│ Business Analyst          │ false              │      94949 │
│ Business Analyst          │ true               │       6218 │
│ Cloud Engineer            │ false              │      28388 │
│ Cloud Engineer            │ true               │       1322 │
│ Data Analyst              │ true               │      27185 │
│ Data Analyst              │ false              │     381455 │
│ Data Engineer             │ true               │      43853 │
│ Data Engineer             │ false              │     348104 │
│ Data Scientist            │ false              │     301671 │
│ Data Scientist            │ true               │      29331 │
│ Machine Learning Engineer │ true               │       4416 │
│ Machine Learning Engineer │ false              │      35212 │
│ Senior Data Analyst       │ true               │       4709 │
│ Senior Data Analyst       │ false              │      54674 │
│ Senior Data Engineer      │ false              │      78180 │
│ Senior Data Engineer      │ true               │      13115 │
│ Senior Data Scientist     │ false              │      63474 │
│ Senior Data Scientist     │ true               │       7403 │
│ Software Engineer         │ false              │      85291 │
│ Software Engineer         │ true               │       6980 │
└───────────────────────────┴────────────────────┴────────────┘
*/

--- SECTION 3: JOINS

---QUESTION #8
---Find the top 10 companies with the most job postings.
---Join job_postings_fact with company_dim.
---Return company_name and total_jobs.
---Order by total_jobs descending.
SELECT
    cd.name AS company_name,
    COUNT(jpf.job_id) AS total_jobs
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
GROUP BY
    company_name
ORDER BY
    total_jobs DESC
LIMIT 10;
/*
┌─────────────────────┬────────────┐
│    company_name     │ total_jobs │
│       varchar       │   int64    │
├─────────────────────┼────────────┤
│ beBee Careers       │      32224 │
│ Emprego             │       6669 │
│ Dice                │       6568 │
│ Capital One         │       6332 │
│ Amazon              │       6204 │
│ Listopro            │       5109 │
│ Harnham             │       4993 │
│ Insight Global      │       4693 │
│ Booz Allen Hamilton │       4678 │
│ Walmart             │       4014 │
└─────────────────────┴────────────┘
*/

---QUESTION #9
---For each company, return total_jobs, max_salary, min_salary, and avg_salary.
---Only include jobs where salary_year_avg is not null.
---Order by total_jobs descending.
SELECT
    cd.name AS company_name,
    COUNT(jpf.job_id) AS total_jobs,
    ROUND(MAX(jpf.salary_year_avg)) AS max_salary,
    ROUND(MIN(jpf.salary_year_avg)) AS min_salary,
    ROUND(AVG(jpf.salary_year_avg)) AS avg_salary
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    jpf.salary_year_avg IS NOT NULL
GROUP BY
    cd.name
ORDER BY
    total_jobs DESC;
/*
┌────────────────────────────────────────┬────────────┬────────────┬────────────┬────────────┐
│              company_name              │ total_jobs │ max_salary │ min_salary │ avg_salary │
│                varchar                 │   int64    │   double   │   double   │   double   │
├────────────────────────────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Incredible Health, Inc.                │       1299 │   155000.0 │    60000.0 │    93918.0 │
│ Jobot                                  │        624 │   312500.0 │    55000.0 │   133008.0 │
│ Capital One                            │        623 │   348000.0 │    58926.0 │   184812.0 │
│ Robert Half                            │        557 │   210000.0 │    41000.0 │   113324.0 │
│ Walmart                                │        542 │   312000.0 │    70000.0 │   156057.0 │
│ TikTok                                 │        505 │   395280.0 │    81312.0 │   203560.0 │
│ Lensa                                  │        466 │   273000.0 │    45870.0 │   137974.0 │
│ Booz Allen Hamilton                    │        464 │   250000.0 │    52100.0 │   122908.0 │
│ Get It Recruit - Information Technolo… │        438 │   238500.0 │    36000.0 │   107477.0 │
│ CareerBuilder                          │        411 │   200000.0 │    50000.0 │    98334.0 │
│ CyberCoders                            │        401 │   250000.0 │    60000.0 │   134538.0 │
│ Meta                                   │        371 │   475000.0 │    45000.0 │   190172.0 │
│ Insight Global                         │        342 │   205000.0 │    35000.0 │   111289.0 │
│ CVS Health                             │        341 │   260590.0 │    43888.0 │   136504.0 │
│ Motion Recruitment                     │        336 │   325000.0 │    50500.0 │   144817.0 │
│ EY                                     │        284 │   267000.0 │    40000.0 │   124273.0 │
│ Harnham                                │        283 │   325000.0 │    60000.0 │   166475.0 │
│ Citi                                   │        264 │   235040.0 │    40000.0 │   128021.0 │
│ SynergisticIT                          │        263 │   150000.0 │    50000.0 │    99409.0 │
│ Amazon                                 │        220 │   268500.0 │    45760.0 │   151388.0 │
│  ·                                     │          · │       ·    │       ·    │       ·    │
│  ·                                     │          · │       ·    │       ·    │       ·    │
│  ·                                     │          · │       ·    │       ·    │       ·    │
│ HCA.                                   │          1 │    70000.0 │    70000.0 │    70000.0 │
│ North East Medical Services            │          1 │   102995.0 │   102995.0 │   102995.0 │
│ Linklaters                             │          1 │   178500.0 │   178500.0 │   178500.0 │
│ The Steely Group                       │          1 │   165000.0 │   165000.0 │   165000.0 │
│ Roger Ward - San Antonio Inc.          │          1 │    42500.0 │    42500.0 │    42500.0 │
│ Critical Path Institute                │          1 │   100000.0 │   100000.0 │   100000.0 │
│ Hireups                                │          1 │   100000.0 │   100000.0 │   100000.0 │
│ Icon VendorPass and Affiliates         │          1 │    60000.0 │    60000.0 │    60000.0 │
│ The Jacobson Group                     │          1 │    87500.0 │    87500.0 │    87500.0 │
│ Blenheim Chalcot India                 │          1 │   121217.0 │   121217.0 │   121217.0 │
│ Mediant Health Resources               │          1 │    75000.0 │    75000.0 │    75000.0 │
│ Naval Nuclear Laboratory               │          1 │    85900.0 │    85900.0 │    85900.0 │
│ Mentra                                 │          1 │    76500.0 │    76500.0 │    76500.0 │
│ Reviewshake, Inc.                      │          1 │    58000.0 │    58000.0 │    58000.0 │
│ University of Wyoming                  │          1 │    58819.0 │    58819.0 │    58819.0 │
│ Perry Lynn Consulting, LLC             │          1 │    62500.0 │    62500.0 │    62500.0 │
│ Solegis, Inc.                          │          1 │   132500.0 │   132500.0 │   132500.0 │
│ EMG Acquisitions                       │          1 │    65000.0 │    65000.0 │    65000.0 │
│ Los Angeles Metro                      │          1 │   130104.0 │   130104.0 │   130104.0 │
│ Steward Health Care                    │          1 │   106065.0 │   106065.0 │   106065.0 │
└────────────────────────────────────────┴────────────┴────────────┴────────────┴────────────┘
*/

---QUESTION #10
---Find all jobs whose company_id does not match a company in company_dim.
---Return company_id and total_jobs.
---Order by total_jobs descending.
SELECT
    COUNT(jpf.job_id) AS total_jobs,
    jpf.company_id
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
/*
┌────────────┬────────────┐
│ total_jobs │ company_id │
│   int64    │   int32    │
└────────────┴────────────┘
*/

--- SECTION 4: SKILLS ANALYSIS
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
│ job_posted_date       timestamp          │
│ job_no_degree_mention boolean            │
│ job_health_insurance  boolean            │
│ job_country           varchar            │
│ salary_rate           varchar            │
│ salary_year_avg       double             │
│ salary_hour_avg       double             │
└──────────────────────────────────────────┘
DESCRIBE skills_job_dim;
┌───────────────────────────┐
│      skills_job_dim       │
│                           │
│ skill_id integer not null │
│ job_id   integer not null │
└───────────────────────────┘
DESCRIBE skills_dim;
┌───────────────────────────┐
│        skills_dim         │
│                           │
│ skill_id integer not null │
│ skills   varchar          │
│ type     varchar          │
└───────────────────────────┘
*/

---QUESTION #11
---Find the top 20 most demanded skills across all jobs.
---Return skill_name and demand_count.
---Use skills_job_dim and skills_dim.
---Order by demand_count descending.
SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
GROUP BY
    sd.skills
ORDER BY
    demand_count DESC
LIMIT 20;

/*
┌────────────┬──────────────┐
│ skill_name │ demand_count │
│  varchar   │    int64     │
├────────────┼──────────────┤
│ python     │       759081 │
│ sql        │       758824 │
│ aws        │       302245 │
│ azure      │       280137 │
│ excel      │       245645 │
│ tableau    │       241876 │
│ r          │       237602 │
│ spark      │       222464 │
│ power bi   │       205785 │
│ java       │       164723 │
│ sas        │       146388 │
│ snowflake  │       122174 │
│ databricks │       121834 │
│ hadoop     │       118739 │
│ scala      │       109664 │
│ gcp        │       108917 │
│ kafka      │        96902 │
│ git        │        95940 │
│ airflow    │        94671 │
│ oracle     │        86351 │
└────────────┴──────────────┘
*/

---QUESTION #12
---Find the top 20 most demanded skills for Data Analyst jobs.
---Return skill_name and demand_count.
---Order by demand_count descending.
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
    skill_name
ORDER BY
    demand_count DESC
LIMIT 20;
/*
┌────────────┬──────────────┐
│ skill_name │ demand_count │
│  varchar   │    int64     │
├────────────┼──────────────┤
│ sql        │       180369 │
│ excel      │       131822 │
│ python     │       116082 │
│ tableau    │        90588 │
│ power bi   │        84353 │
│ r          │        58385 │
│ sas        │        50742 │
│ powerpoint │        25316 │
│ word       │        25111 │
│ azure      │        21613 │
│ sap        │        20903 │
│ aws        │        18967 │
│ oracle     │        18966 │
│ sql server │        15130 │
│ go         │        14433 │
│ flow       │        14097 │
│ looker     │        13875 │
│ snowflake  │        13207 │
│ vba        │        12066 │
│ java       │        10255 │
└────────────┴──────────────┘
*/

---QUESTION #13
---Find the top 20 skills with the highest average salary for Data Analyst jobs.
---Only include jobs where salary_year_avg is not null.
---Return skill_name and avg_salary.
---Order by avg_salary descending.
SELECT
    sd.skills AS skill_name,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
WHERE
    salary_year_avg IS NOT NULL
    AND job_title_short = 'Data Analyst'
GROUP BY
    sd.skills
ORDER BY
    avg_salary DESC
LIMIT 20;
/*
┌──────────────┬────────────┐
│  skill_name  │ avg_salary │
│   varchar    │   double   │
├──────────────┼────────────┤
│ fastapi      │   212500.0 │
│ svn          │   185000.0 │
│ blazor       │   161000.0 │
│ apl          │   155000.0 │
│ mxnet        │   149000.0 │
│ graphql      │   137699.0 │
│ typescript   │   135520.0 │
│ asp.net core │   130500.0 │
│ dynamodb     │   129970.0 │
│ solidity     │   128313.0 │
│ react.js     │   128000.0 │
│ terraform    │   127119.0 │
│ atlassian    │   124636.0 │
│ node         │   124293.0 │
│ hugging face │   123950.0 │
│ watson       │   123411.0 │
│ golang       │   122203.0 │
│ dplyr        │   122158.0 │
│ twilio       │   120250.0 │
│ mattermost   │   120000.0 │
└──────────────┴────────────┘
*/
---QUESTION #14
---Find Data Analyst skills where demand_count is at least 10.
---Return skill_name, demand_count, and avg_salary.
---Only include jobs where salary_year_avg is not null.
---Order by avg_salary descending.
SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
WHERE
    jpf.job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
GROUP BY
    skill_name
HAVING
    demand_count >= 10
ORDER BY
    avg_salary DESC;
/*
┌─────────────────┬──────────────┬────────────┐
│   skill_name    │ demand_count │ avg_salary │
│     varchar     │    int64     │   double   │
├─────────────────┼──────────────┼────────────┤
│ graphql         │           49 │   137699.0 │
│ typescript      │           12 │   135520.0 │
│ dynamodb        │           23 │   129970.0 │
│ terraform       │           32 │   127119.0 │
│ atlassian       │           32 │   124636.0 │
│ node            │           11 │   124293.0 │
│ dplyr           │           10 │   122158.0 │
│ neo4j           │           29 │   119579.0 │
│ perl            │           44 │   118653.0 │
│ no-sql          │           11 │   118553.0 │
│ elasticsearch   │           31 │   118378.0 │
│ kafka           │          111 │   116062.0 │
│ zoom            │           71 │   116061.0 │
│ splunk          │           35 │   115501.0 │
│ snowflake       │          671 │   112949.0 │
│ spark           │          460 │   111904.0 │
│ php             │           47 │   111687.0 │
│ databricks      │          369 │   111581.0 │
│ confluence      │          127 │   111405.0 │
│ phoenix         │           40 │   111096.0 │
│   ·             │            · │       ·    │
│   ·             │            · │       ·    │
│   ·             │            · │       ·    │
│ unity           │           26 │    86634.0 │
│ ruby            │           26 │    86606.0 │
│ css             │           89 │    86176.0 │
│ powerpoint      │         1124 │    86056.0 │
│ sheets          │          304 │    85303.0 │
│ firebase        │           34 │    84853.0 │
│ assembly        │           51 │    84790.0 │
│ ms access       │          134 │    84013.0 │
│ html            │          138 │    83824.0 │
│ spss            │          427 │    83565.0 │
│ word            │         1101 │    81267.0 │
│ terminal        │           97 │    81073.0 │
│ tidyverse       │           12 │    79900.0 │
│ microsoft teams │           33 │    79393.0 │
│ planner         │           25 │    79144.0 │
│ smartsheet      │           45 │    78637.0 │
│ spreadsheet     │          206 │    78020.0 │
│ outlook         │          410 │    77834.0 │
│ macos           │           14 │    77088.0 │
│ wire            │           16 │    74744.0 │
└─────────────────┴──────────────┴────────────┘
*/

---QUESTION #15
---For remote jobs only, find the top 20 skills by demand_count.
---Return skill_name, demand_count, avg_salary, and max_salary.
---Only include jobs where salary_year_avg is not null.
---Only include skills with demand_count >= 10.
---Order by demand_count descending.
SELECT
    sd.skills AS skill_name,
    COUNT(jpf.job_id) AS demand_count,
    ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
    ROUND(MAX(jpf.salary_year_avg), 0) AS max_salary
FROM
    job_postings_fact AS jpf
JOIN skills_job_dim AS sjd
    ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd
    ON sjd.skill_id = sd.skill_id
WHERE 
    jpf.salary_year_avg IS NOT NULL
    AND jpf.job_work_from_home = TRUE
GROUP BY 
    sd.skills
HAVING
    demand_count >= 10
ORDER BY
    demand_count DESC
LIMIT 20;
/*
┌────────────┬──────────────┬────────────┬────────────┐
│ skill_name │ demand_count │ avg_salary │ max_salary │
│  varchar   │    int64     │   double   │   double   │
├────────────┼──────────────┼────────────┼────────────┤
│ python     │         4627 │   136370.0 │   680000.0 │
│ sql        │         4411 │   130300.0 │   680000.0 │
│ aws        │         2072 │   141076.0 │   375000.0 │
│ r          │         1594 │   131401.0 │   680000.0 │
│ tableau    │         1512 │   122359.0 │   375000.0 │
│ azure      │         1275 │   135349.0 │   320000.0 │
│ spark      │         1274 │   146668.0 │   445000.0 │
│ snowflake  │         1022 │   141943.0 │   348000.0 │
│ excel      │          932 │   104727.0 │   385000.0 │
│ sas        │          788 │   117069.0 │   288000.0 │
│ power bi   │          765 │   109239.0 │   265000.0 │
│ airflow    │          758 │   152613.0 │   327330.0 │
│ java       │          741 │   141095.0 │   445000.0 │
│ gcp        │          672 │   142915.0 │   325000.0 │
│ databricks │          666 │   138343.0 │   288000.0 │
│ redshift   │          636 │   134714.0 │   288000.0 │
│ looker     │          552 │   131334.0 │   264000.0 │
│ hadoop     │          542 │   139482.0 │   375000.0 │
│ scala      │          536 │   151919.0 │   445000.0 │
│ kafka      │          490 │   150463.0 │   325000.0 │
└────────────┴──────────────┴────────────┴────────────┘
*/

--- SECTION 5: CTES

---QUESTION #16
---Use a CTE to calculate the number of remote jobs for each job_title_short.
---Return job_title_short and total_remote_jobs.
---Order by total_remote_jobs descending.
WITH calculate_remote AS (
    SELECT
        COUNT(job_id) AS total_remote_jobs,
        job_title_short
    FROM
        job_postings_fact
    WHERE
        job_work_from_home = TRUE
    GROUP BY
    job_title_short
)
SELECT
    total_remote_jobs,
    job_title_short
FROM
    calculate_remote
ORDER BY
    total_remote_jobs DESC;
/*
┌───────────────────┬────────────────────┬───────────────────────────┐
│ total_remote_jobs │ job_work_from_home │      job_title_short      │
│       int64       │      boolean       │          varchar          │
├───────────────────┼────────────────────┼───────────────────────────┤
│             43853 │ true               │ Data Engineer             │
│             29331 │ true               │ Data Scientist            │
│             27185 │ true               │ Data Analyst              │
│             13115 │ true               │ Senior Data Engineer      │
│              7403 │ true               │ Senior Data Scientist     │
│              6980 │ true               │ Software Engineer         │
│              6218 │ true               │ Business Analyst          │
│              4709 │ true               │ Senior Data Analyst       │
│              4416 │ true               │ Machine Learning Engineer │
│              1322 │ true               │ Cloud Engineer            │
└───────────────────┴────────────────────┴───────────────────────────┘
*/

---QUESTION #17
---Use a CTE to find the top 10 companies with more than 100 job postings.
---Return company_name and total_jobs.
---Order by total_jobs descending.
WITH top_companies AS (
    SELECT
        cd.name AS company_name,
        COUNT(jpf.job_id) AS total_jobs
    FROM
        job_postings_fact AS jpf
    JOIN company_dim AS cd
        ON jpf.company_id = cd.company_id
    GROUP BY
        cd.name
    HAVING
        COUNT(jpf.job_id) > 100
)
SELECT
    company_name,
    total_jobs
FROM
    top_companies
ORDER BY
    total_jobs DESC
LIMIT 10;
/*
┌─────────────────────┬────────────┐
│    company_name     │ total_jobs │
│       varchar       │   int64    │
├─────────────────────┼────────────┤
│ beBee Careers       │      32224 │
│ Emprego             │       6669 │
│ Dice                │       6568 │
│ Capital One         │       6332 │
│ Amazon              │       6204 │
│ Listopro            │       5109 │
│ Harnham             │       4993 │
│ Insight Global      │       4693 │
│ Booz Allen Hamilton │       4678 │
│ Walmart             │       4014 │
└─────────────────────┴────────────┘
*/

---QUESTION #18
---Use a CTE named skill_stats.
---For Data Analyst jobs, return skill_name, demand_count, avg_salary, and score.
---score should equal demand_count * avg_salary.
---Only include rows where salary_year_avg is not null.
---Only include skills with demand_count >= 10.
---Order by score descending.
WITH skill_stats AS (
    SELECT
        sd.skills AS skill_name,
        COUNT(jpf.job_id) AS demand_count,
        ROUND(AVG(jpf.salary_year_avg), 0) AS avg_salary,
        COUNT(jpf.job_id) * ROUND(AVG(jpf.salary_year_avg), 0) AS score
    FROM
        job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    WHERE
        jpf.salary_year_avg IS NOT null
        AND job_title_short = 'Data Analyst'
    GROUP BY
        sd.skills
    HAVING
        COUNT(jpf.job_id) >= 10
    ORDER BY
        score DESC
)
SELECT
    skill_name,
    demand_count,
    avg_salary,
    score
FROM 
    skill_stats;
/*
┌─────────────┬──────────────┬────────────┬──────────────┐
│ skill_name  │ demand_count │ avg_salary │    score     │
│   varchar   │    int64     │   double   │    double    │
├─────────────┼──────────────┼────────────┼──────────────┤
│ python      │        28943 │   133094.0 │ 3852139642.0 │
│ sql         │        29027 │   125970.0 │ 3656531190.0 │
│ aws         │        11308 │   138353.0 │ 1564495724.0 │
│ r           │        11166 │   127800.0 │ 1427014800.0 │
│ tableau     │        10830 │   117396.0 │ 1271398680.0 │
│ spark       │         8649 │   143955.0 │ 1245066795.0 │
│ azure       │         8625 │   133116.0 │ 1148125500.0 │
│ excel       │         9858 │    98093.0 │  967000794.0 │
│ java        │         6286 │   137777.0 │  866066222.0 │
│ snowflake   │         6049 │   140350.0 │  848977150.0 │
│ sas         │         6740 │   113089.0 │  762219860.0 │
│ power bi    │         6998 │   108249.0 │  757526502.0 │
│ hadoop      │         4685 │   142243.0 │  666408455.0 │
│ scala       │         4377 │   146777.0 │  642442929.0 │
│ databricks  │         4201 │   135935.0 │  571062935.0 │
│ kafka       │         3741 │   147860.0 │  553144260.0 │
│ nosql       │         3654 │   139158.0 │  508483332.0 │
│ airflow     │         3330 │   145681.0 │  485117730.0 │
│ redshift    │         3379 │   143036.0 │  483318644.0 │
│ gcp         │         3334 │   136132.0 │  453864088.0 │
│  ·          │            · │       ·    │        ·     │
│  ·          │            · │       ·    │        ·     │
│  ·          │            · │       ·    │        ·     │
│ pulumi      │           25 │   128960.0 │    3224000.0 │
│ flutter     │           22 │   120145.0 │    2643190.0 │
│ twilio      │           18 │   134241.0 │    2416338.0 │
│ clojure     │           17 │   136253.0 │    2316301.0 │
│ dart        │           21 │   104561.0 │    2195781.0 │
│ vue.js      │           20 │   102287.0 │    2045740.0 │
│ ringcentral │           20 │    96588.0 │    1931760.0 │
│ symphony    │           16 │   117253.0 │    1876048.0 │
│ openstack   │           14 │   130316.0 │    1824424.0 │
│ colocation  │           19 │    94530.0 │    1796070.0 │
│ fortran     │           15 │   116283.0 │    1744245.0 │
│ npm         │           15 │   103421.0 │    1551315.0 │
│ drupal      │           14 │   110718.0 │    1550052.0 │
│ elixir      │           13 │   114740.0 │    1491620.0 │
│ electron    │           12 │   118311.0 │    1419732.0 │
│ codecommit  │           10 │   140883.0 │    1408830.0 │
│ heroku      │           10 │   122045.0 │    1220450.0 │
│ workfront   │           11 │   103717.0 │    1140887.0 │
│ cobol       │           11 │   101532.0 │    1116852.0 │
│ sass        │           10 │   101710.0 │    1017100.0 │
└─────────────┴──────────────┴────────────┴──────────────┘
*/

--- SECTION 6: WINDOW FUNCTIONS

---QUESTION #19
---For each job row with a salary, show:
---job_id, job_title_short, salary_year_avg, and avg_salary_for_title.
---Use AVG() OVER(PARTITION BY job_title_short).
SELECT
    job_id,
    job_title_short,
    salary_year_avg,
    AVG(salary_year_avg) OVER(
        PARTITION BY job_title_short
    ) AS avg_salary_for_title
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL;
/*
┌─────────┬───────────────────────────┬─────────────────┬──────────────────────┐
│ job_id  │      job_title_short      │ salary_year_avg │ avg_salary_for_title │
│  int32  │          varchar          │     double      │        double        │
├─────────┼───────────────────────────┼─────────────────┼──────────────────────┤
│  594714 │ Data Scientist            │        105151.5 │   134324.05013149753 │
│  594737 │ Senior Data Scientist     │        204000.0 │   156390.76072875268 │
│  594739 │ Data Engineer             │        113836.5 │   134867.11449966236 │
│  594837 │ Senior Data Engineer      │        175500.0 │   149222.25039026805 │
│  594873 │ Machine Learning Engineer │         90000.0 │    137331.7497598857 │
│  594921 │ Business Analyst          │         48000.0 │    98660.39627134302 │
│  595008 │ Data Scientist            │        145000.0 │   134324.05013149753 │
│  595146 │ Senior Data Scientist     │        162500.0 │   156390.76072875268 │
│  595205 │ Data Scientist            │        111500.0 │   134324.05013149753 │
│  595304 │ Business Analyst          │         87500.0 │    98660.39627134302 │
│  595331 │ Data Analyst              │         75000.0 │     93223.1844804113 │
│  595469 │ Senior Data Analyst       │         98172.0 │   115799.54319535152 │
│  595470 │ Senior Data Analyst       │         85000.0 │   115799.54319535152 │
│  595480 │ Senior Data Engineer      │        240000.0 │   149222.25039026805 │
│  595484 │ Senior Data Engineer      │        177500.0 │   149222.25039026805 │
│  595571 │ Data Analyst              │        116000.0 │     93223.1844804113 │
│  595581 │ Data Analyst              │        100000.0 │     93223.1844804113 │
│  595586 │ Data Analyst              │         80000.0 │     93223.1844804113 │
│  595595 │ Senior Data Engineer      │        150000.0 │   149222.25039026805 │
│  595667 │ Data Analyst              │         73250.0 │     93223.1844804113 │
│     ·   │      ·                    │            ·    │             ·        │
│     ·   │      ·                    │            ·    │             ·        │
│     ·   │      ·                    │            ·    │             ·        │
│ 1275059 │ Senior Data Engineer      │        175500.0 │   149222.25039026805 │
│ 1275147 │ Data Analyst              │        215500.0 │     93223.1844804113 │
│ 1275148 │ Data Analyst              │        215500.0 │     93223.1844804113 │
│ 1275264 │ Data Scientist            │        172500.0 │   134324.05013149753 │
│ 1275290 │ Data Scientist            │        172500.0 │   134324.05013149753 │
│ 1275421 │ Data Engineer             │        197500.0 │   134867.11449966236 │
│ 1275448 │ Data Engineer             │        197500.0 │   134867.11449966236 │
│ 1275491 │ Business Analyst          │        117500.0 │    98660.39627134302 │
│ 1275494 │ Data Engineer             │        111000.0 │   134867.11449966236 │
│ 1275526 │ Data Engineer             │        111000.0 │   134867.11449966236 │
│ 1275639 │ Data Analyst              │         95305.0 │     93223.1844804113 │
│ 1275641 │ Data Analyst              │         95305.0 │     93223.1844804113 │
│ 1275759 │ Data Analyst              │         62500.0 │     93223.1844804113 │
│ 1275760 │ Data Analyst              │         62500.0 │     93223.1844804113 │
│ 1275796 │ Senior Data Engineer      │        134000.0 │   149222.25039026805 │
│ 1275797 │ Senior Data Engineer      │        134000.0 │   149222.25039026805 │
│ 1275818 │ Data Engineer             │        122500.0 │   134867.11449966236 │
│ 1275834 │ Data Engineer             │        122500.0 │   134867.11449966236 │
│ 1275848 │ Data Engineer             │        135300.0 │   134867.11449966236 │
│ 1275868 │ Data Engineer             │        135300.0 │   134867.11449966236 │
└─────────┴───────────────────────────┴─────────────────┴──────────────────────┘
*/

---QUESTION #20
---Find the highest salary job for each job_title_short.
---Use ROW_NUMBER() with PARTITION BY job_title_short.
---Return job_title_short, job_id, salary_year_avg, and salary_rank.
WITH salary_rank AS (    
    SELECT
        job_title_short,
        job_id,
        salary_year_avg,
        ROW_NUMBER() over(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS salary_rank
    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    job_id,
    salary_year_avg,
    salary_rank
FROM salary_rank
WHERE
    salary_rank = 1
ORDER BY
    salary_year_avg DESC;
/*
┌───────────────────────────┬─────────┬─────────────────┬─────────────┐
│      job_title_short      │ job_id  │ salary_year_avg │ salary_rank │
│          varchar          │  int32  │     double      │    int64    │
├───────────────────────────┼─────────┼─────────────────┼─────────────┤
│ Data Scientist            │  296745 │        960000.0 │           1 │
│ Senior Data Scientist     │  673003 │        890000.0 │           1 │
│ Machine Learning Engineer │ 1575798 │        875000.0 │           1 │
│ Senior Data Engineer      │ 1443865 │        800000.0 │           1 │
│ Data Analyst              │  142665 │        650000.0 │           1 │
│ Data Engineer             │  871759 │        640000.0 │           1 │
│ Senior Data Analyst       │  382322 │        425000.0 │           1 │
│ Software Engineer         │ 1291078 │        425000.0 │           1 │
│ Business Analyst          │  951196 │        390000.0 │           1 │
│ Cloud Engineer            │ 1444286 │        305000.0 │           1 │
└───────────────────────────┴─────────┴─────────────────┴─────────────┘
*/

---QUESTION #21
---Find the top 3 salaries for each job_title_short.
---Use ROW_NUMBER() with PARTITION BY job_title_short.
---Only include rows where salary_year_avg is not null.
WITH top_salaries AS (
    SELECT
        salary_year_avg,
        job_title_short,
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
    salary_year_avg,
    job_title_short,
    salary
FROM top_salaries
WHERE 
    salary <= 3;
/*
┌─────────────────┬───────────────────────────┬────────┐
│ salary_year_avg │      job_title_short      │ salary │
│     double      │          varchar          │ int64  │
├─────────────────┼───────────────────────────┼────────┤
│        875000.0 │ Machine Learning Engineer │      1 │
│        800000.0 │ Machine Learning Engineer │      2 │
│        400000.0 │ Machine Learning Engineer │      3 │
│        425000.0 │ Senior Data Analyst       │      1 │
│        420000.0 │ Senior Data Analyst       │      2 │
│        375000.0 │ Senior Data Analyst       │      3 │
│        305000.0 │ Cloud Engineer            │      1 │
│        287500.0 │ Cloud Engineer            │      2 │
│        280000.0 │ Cloud Engineer            │      3 │
│        650000.0 │ Data Analyst              │      1 │
│        445000.0 │ Data Analyst              │      2 │
│        445000.0 │ Data Analyst              │      3 │
│        425000.0 │ Software Engineer         │      1 │
│        375000.0 │ Software Engineer         │      2 │
│        345875.0 │ Software Engineer         │      3 │
│        640000.0 │ Data Engineer             │      1 │
│        525000.0 │ Data Engineer             │      2 │
│        450000.0 │ Data Engineer             │      3 │
│        960000.0 │ Data Scientist            │      1 │
│        920000.0 │ Data Scientist            │      2 │
│        870000.0 │ Data Scientist            │      3 │
│        390000.0 │ Business Analyst          │      1 │
│        387460.0 │ Business Analyst          │      2 │
│        286000.0 │ Business Analyst          │      3 │
│        800000.0 │ Senior Data Engineer      │      1 │
│        425000.0 │ Senior Data Engineer      │      2 │
│        378500.0 │ Senior Data Engineer      │      3 │
│        890000.0 │ Senior Data Scientist     │      1 │
│        475000.0 │ Senior Data Scientist     │      2 │
│        463500.0 │ Senior Data Scientist     │      3 │
└─────────────────┴───────────────────────────┴────────┘
*/

---QUESTION #22
---Find the lowest salary for each job_title_short.
---Use ROW_NUMBER() ordered by salary_year_avg ascending.
WITH lowest_salary AS (
    SELECT
        salary_year_avg,
        job_title_short,
        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg ASC
        ) AS salary_rank
    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    salary_rank
FROM
lowest_salary
WHERE
    salary_rank = 1;

---QUESTION #23
---Use RANK() to rank salaries within each job_title_short.
---Return job_title_short, salary_year_avg, and rank_num.
---Order salaries from highest to lowest inside each job title.
WITH rank_num AS (
    SELECT
        job_title_short,
        salary_year_avg,

        rank() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS rank_salaries
        FROM 
            job_postings_fact
        WHERE
            salary_year_avg IS NOT NULL
)

SELECT
    job_title_short,
    salary_year_avg,
    rank_salaries
FROM
    rank_num
ORDER BY 
    salary_year_avg DESC;
/*
┌───────────────────────────┬─────────────────┬───────────────┐
│      job_title_short      │ salary_year_avg │ rank_salaries │
│          varchar          │     double      │     int64     │
├───────────────────────────┼─────────────────┼───────────────┤
│ Data Scientist            │        960000.0 │             1 │
│ Data Scientist            │        920000.0 │             2 │
│ Senior Data Scientist     │        890000.0 │             1 │
│ Machine Learning Engineer │        875000.0 │             1 │
│ Data Scientist            │        870000.0 │             3 │
│ Data Scientist            │        850000.0 │             4 │
│ Senior Data Engineer      │        800000.0 │             1 │
│ Machine Learning Engineer │        800000.0 │             2 │
│ Data Scientist            │        680000.0 │             5 │
│ Data Analyst              │        650000.0 │             1 │
│ Data Engineer             │        640000.0 │             1 │
│ Data Scientist            │        640000.0 │             6 │
│ Data Scientist            │        585000.0 │             7 │
│ Data Scientist            │        550000.0 │             8 │
│ Data Engineer             │        525000.0 │             2 │
│ Data Scientist            │        525000.0 │             9 │
│ Senior Data Scientist     │        475000.0 │             2 │
│ Data Scientist            │        475000.0 │            10 │
│ Senior Data Scientist     │        463500.0 │             3 │
│ Data Engineer             │        450000.0 │             3 │
│       ·                   │            ·    │             · │
│       ·                   │            ·    │             · │
│       ·                   │            ·    │             · │
│ Software Engineer         │         22000.0 │          1577 │
│ Machine Learning Engineer │         22000.0 │          1334 │
│ Software Engineer         │         21880.0 │          1578 │
│ Business Analyst          │         21750.0 │          1961 │
│ Data Analyst              │         21000.0 │         13596 │
│ Data Analyst              │         21000.0 │         13596 │
│ Data Scientist            │         20100.5 │         12622 │
│ Data Scientist            │         20100.5 │         12622 │
│ Data Engineer             │         20000.0 │         10548 │
│ Data Analyst              │         20000.0 │         13598 │
│ Cloud Engineer            │         19200.0 │           218 │
│ Data Analyst              │         19000.0 │         13599 │
│ Data Engineer             │         18000.0 │         10549 │
│ Data Analyst              │         18000.0 │         13600 │
│ Data Scientist            │         17772.0 │         12624 │
│ Data Scientist            │         16800.0 │         12625 │
│ Business Analyst          │         16500.0 │          1962 │
│ Data Engineer             │         15000.0 │         10550 │
│ Data Engineer             │         15000.0 │         10550 │
│ Cloud Engineer            │         15000.0 │           219 │
└───────────────────────────┴─────────────────┴───────────────┘
*/

---QUESTION #24
---Use DENSE_RANK() to rank salaries within each job_title_short.
---Return job_title_short, salary_year_avg, and dense_rank.
---Order salaries from highest to lowest inside each job title.
WITH rank_salaries AS (
    SELECT 
        job_title_short,
        salary_year_avg,

        DENSE_RANK() OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg DESC
        ) AS rank_salaries
    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    rank_salaries
FROM
    rank_salaries
ORDER BY
    job_title_short,
    rank_salaries;
/*
┌───────────────────────────┬─────────────────┬───────────────┐
│      job_title_short      │ salary_year_avg │ rank_salaries │
│          varchar          │     double      │     int64     │
├───────────────────────────┼─────────────────┼───────────────┤
│ Data Scientist            │        960000.0 │             1 │
│ Data Scientist            │        920000.0 │             2 │
│ Senior Data Scientist     │        890000.0 │             1 │
│ Machine Learning Engineer │        875000.0 │             1 │
│ Data Scientist            │        870000.0 │             3 │
│ Data Scientist            │        850000.0 │             4 │
│ Senior Data Engineer      │        800000.0 │             1 │
│ Machine Learning Engineer │        800000.0 │             2 │
│ Data Scientist            │        680000.0 │             5 │
│ Data Analyst              │        650000.0 │             1 │
│ Data Engineer             │        640000.0 │             1 │
│ Data Scientist            │        640000.0 │             6 │
│ Data Scientist            │        585000.0 │             7 │
│ Data Scientist            │        550000.0 │             8 │
│ Data Engineer             │        525000.0 │             2 │
│ Data Scientist            │        525000.0 │             9 │
│ Senior Data Scientist     │        475000.0 │             2 │
│ Data Scientist            │        475000.0 │            10 │
│ Senior Data Scientist     │        463500.0 │             3 │
│ Data Engineer             │        450000.0 │             3 │
│       ·                   │            ·    │             · │
│       ·                   │            ·    │             · │
│       ·                   │            ·    │             · │
│ Software Engineer         │         22000.0 │          1577 │
│ Machine Learning Engineer │         22000.0 │          1334 │
│ Software Engineer         │         21880.0 │          1578 │
│ Business Analyst          │         21750.0 │          1961 │
│ Data Analyst              │         21000.0 │         13596 │
│ Data Analyst              │         21000.0 │         13596 │
│ Data Scientist            │         20100.5 │         12622 │
│ Data Scientist            │         20100.5 │         12622 │
│ Data Engineer             │         20000.0 │         10548 │
│ Data Analyst              │         20000.0 │         13598 │
│ Cloud Engineer            │         19200.0 │           218 │
│ Data Analyst              │         19000.0 │         13599 │
│ Data Engineer             │         18000.0 │         10549 │
│ Data Analyst              │         18000.0 │         13600 │
│ Data Scientist            │         17772.0 │         12624 │
│ Data Scientist            │         16800.0 │         12625 │
│ Business Analyst          │         16500.0 │          1962 │
│ Data Engineer             │         15000.0 │         10550 │
│ Data Engineer             │         15000.0 │         10550 │
│ Cloud Engineer            │         15000.0 │           219 │
└───────────────────────────┴─────────────────┴───────────────┘
*/

---QUESTION #25
---Calculate a running total of salary_year_avg within each job_title_short.
---Use SUM() OVER(PARTITION BY job_title_short ORDER BY salary_year_avg).
---Only include rows where salary_year_avg is not null.
WITH running_total AS (
    SELECT
        job_title_short,
        salary_year_avg,

        SUM(salary_year_avg) OVER(
            PARTITION BY job_title_short
            ORDER BY salary_year_avg ASC
        ) AS total_sum

    FROM
        job_postings_fact
    WHERE
        salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    salary_year_avg,
    total_sum
FROM
    running_total
ORDER BY
    job_title_short,
    total_sum;
/*
┌───────────────────┬─────────────────┬──────────────────┐
│  job_title_short  │ salary_year_avg │    total_sum     │
│      varchar      │     double      │      double      │
├───────────────────┼─────────────────┼──────────────────┤
│ Business Analyst  │         16500.0 │          16500.0 │
│ Business Analyst  │         21750.0 │          38250.0 │
│ Business Analyst  │         23000.0 │          61250.0 │
│ Business Analyst  │         24000.0 │          85250.0 │
│ Business Analyst  │         25000.0 │         135250.0 │
│ Business Analyst  │         25000.0 │         135250.0 │
│ Business Analyst  │         29900.0 │         165150.0 │
│ Business Analyst  │         30000.0 │         255150.0 │
│ Business Analyst  │         30000.0 │         255150.0 │
│ Business Analyst  │         30000.0 │         255150.0 │
│ Business Analyst  │         31000.0 │         286150.0 │
│ Business Analyst  │         32000.0 │         350150.0 │
│ Business Analyst  │         32000.0 │         350150.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34400.0 │         556550.0 │
│ Business Analyst  │         34560.0 │         591110.0 │
│        ·          │            ·    │             ·    │
│        ·          │            ·    │             ·    │
│        ·          │            ·    │             ·    │
│ Software Engineer │        275000.0 │ 218516354.203125 │
│ Software Engineer │        275000.0 │ 218516354.203125 │
│ Software Engineer │        275000.0 │ 218516354.203125 │
│ Software Engineer │        275000.0 │ 218516354.203125 │
│ Software Engineer │        275000.0 │ 218516354.203125 │
│ Software Engineer │        276000.0 │ 218792354.203125 │
│ Software Engineer │        287000.0 │ 219079354.203125 │
│ Software Engineer │        288500.0 │ 219367854.203125 │
│ Software Engineer │        295000.0 │ 219662854.203125 │
│ Software Engineer │        300000.0 │ 219962854.203125 │
│ Software Engineer │        303000.0 │ 220265854.203125 │
│ Software Engineer │        307710.0 │ 220573564.203125 │
│ Software Engineer │        316000.0 │ 220889564.203125 │
│ Software Engineer │        317000.0 │ 221523564.203125 │
│ Software Engineer │        317000.0 │ 221523564.203125 │
│ Software Engineer │        318500.0 │ 221842064.203125 │
│ Software Engineer │        320000.0 │ 222162064.203125 │
│ Software Engineer │        345875.0 │ 222507939.203125 │
│ Software Engineer │        375000.0 │ 222882939.203125 │
│ Software Engineer │        425000.0 │ 223307939.203125 │
└───────────────────┴─────────────────┴──────────────────┘
*/

---QUESTION #26
---Calculate the percentage of each job_title_short compared to total jobs.
---Return job_title_short, total_jobs_by_title, total_jobs, and job_title_percentage.
---Use COUNT(*) and a window function.
---Order by job_title_percentage descending.
WITH percentage_calculation AS (
    SELECT
        job_title_short,
        COUNT(job_id) AS total_jobs,
        ROUND(
            COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(),
            2
        ) AS job_title_percentage
    FROM
        job_postings_fact
    GROUP BY 
        job_title_short
)

SELECT
    job_title_short,
    total_jobs,
    job_title_percentage
FROM 
    percentage_calculation;   
/*
┌───────────────────────────┬────────────┬──────────────────────┐
│      job_title_short      │ total_jobs │ job_title_percentage │
│          varchar          │   int64    │        double        │
├───────────────────────────┼────────────┼──────────────────────┤
│ Senior Data Analyst       │      59383 │                 3.67 │
│ Machine Learning Engineer │      39628 │                 2.45 │
│ Cloud Engineer            │      29710 │                 1.84 │
│ Data Analyst              │     408640 │                25.29 │
│ Software Engineer         │      92271 │                 5.71 │
│ Senior Data Engineer      │      91295 │                 5.65 │
│ Data Engineer             │     391957 │                24.26 │
│ Data Scientist            │     331002 │                20.48 │
│ Business Analyst          │     101167 │                 6.26 │
│ Senior Data Scientist     │      70877 │                 4.39 │
└───────────────────────────┴────────────┴──────────────────────┘
*/
--- SECTION 7: CASE WHEN

---QUESTION #27
---Create a salary_category column:
---High Salary if salary_year_avg >= 150000
---Medium Salary if salary_year_avg >= 80000
---Low Salary otherwise
---Only include rows where salary_year_avg is not null.
SELECT
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
/*
┌─────────────────┬─────────────────┐
│ salary_year_avg │ salary_category │
│     double      │     varchar     │
├─────────────────┼─────────────────┤
│        110000.0 │ Medium Salary   │
│         65000.0 │ Low Salary      │
│         90000.0 │ Medium Salary   │
│         55000.0 │ Low Salary      │
│        120531.0 │ Medium Salary   │
│        300000.0 │ High Salary     │
│         51000.0 │ Low Salary      │
│        133500.0 │ Medium Salary   │
│         77500.0 │ Low Salary      │
│        125000.0 │ Medium Salary   │
│        202500.0 │ High Salary     │
│        165000.0 │ High Salary     │
│        105000.0 │ Medium Salary   │
│        175000.0 │ High Salary     │
│        175000.0 │ High Salary     │
│         81167.0 │ Medium Salary   │
│        165000.0 │ High Salary     │
│        113000.0 │ Medium Salary   │
│        129982.0 │ Medium Salary   │
│        137150.0 │ Medium Salary   │
│            ·    │       ·         │
│            ·    │       ·         │
│            ·    │       ·         │
│        102500.0 │ Medium Salary   │
│        165000.0 │ High Salary     │
│        179126.5 │ High Salary     │
│        162000.0 │ High Salary     │
│        133120.0 │ Medium Salary   │
│         45000.0 │ Low Salary      │
│    176938.65625 │ High Salary     │
│    176938.65625 │ High Salary     │
│    176938.65625 │ High Salary     │
│        132704.0 │ Medium Salary   │
│         95000.0 │ Medium Salary   │
│         92500.0 │ Medium Salary   │
│        170000.0 │ High Salary     │
│        245000.0 │ High Salary     │
│         50000.0 │ Low Salary      │
│        158000.0 │ High Salary     │
│        135000.0 │ Medium Salary   │
│        105500.0 │ Medium Salary   │
│         70700.0 │ Low Salary      │
│        108267.0 │ Medium Salary   │
└─────────────────┴─────────────────┘
*/

---QUESTION #28
---Create a remote_status column:
---Remote if job_location is 'Anywhere'
---Onsite if job_location is not 'Anywhere'
---Unknown if job_location is null or blank.
SELECT
    job_location,
    CASE 
        WHEN job_location IS NULL 
            OR TRIM(job_location) = '' THEN 'Unknown'
        WHEN TRIM(job_location) = 'Anywhere' THEN 'Remote'
        ELSE 'Onsite'
    END AS remote_status
FROM
    job_postings_fact;
/*
┌──────────────────────────────────────────────────────────┬───────────────┐
│                       job_location                       │ remote_status │
│                         varchar                          │    varchar    │
├──────────────────────────────────────────────────────────┼───────────────┤
│ New York, NY                                             │ Onsite        │
│ Washington, DC                                           │ Onsite        │
│ Fairfax, VA                                              │ Onsite        │
│ Worcester, MA                                            │ Onsite        │
│ Sunnyvale, CA                                            │ Onsite        │
│ Torrance, CA                                             │ Onsite        │
│ San Francisco, CA                                        │ Onsite        │
│ Pleasanton, CA                                           │ Onsite        │
│ Rosemead, CA                                             │ Onsite        │
│ Thousand Oaks, CA                                        │ Onsite        │
│ Vandenberg AFB, CA                                       │ Onsite        │
│ Stanford, CA                                             │ Onsite        │
│ Irvine, CA                                               │ Onsite        │
│ San Jose, CA                                             │ Onsite        │
│ Fullerton, CA                                            │ Onsite        │
│ Pasadena, CA                                             │ Onsite        │
│ Santa Clara, CA                                          │ Onsite        │
│ San Francisco, CA                                        │ Onsite        │
│ Sunnyvale, CA                                            │ Onsite        │
│ Los Angeles, CA                                          │ Onsite        │
│        ·                                                 │   ·           │
│        ·                                                 │   ·           │
│        ·                                                 │   ·           │
│ Dhaka, Bangladesh                                        │ Onsite        │
│ Casalecchio di Reno, Metropolitan City of Bologna, Italy │ Onsite        │
│ Milan, Metropolitan City of Milan, Italy                 │ Onsite        │
│ Fes, Morocco                                             │ Onsite        │
│ Madrid, Spain                                            │ Onsite        │
│ Sri Lanka                                                │ Onsite        │
│ Anywhere                                                 │ Remote        │
│ Moscow, Russia                                           │ Onsite        │
│ Nepal                                                    │ Onsite        │
│ Prague, Czechia                                          │ Onsite        │
│ Prague, Czechia                                          │ Onsite        │
│ Olomouc, Czechia                                         │ Onsite        │
│ Dar es Salaam, Tanzania                                  │ Onsite        │
│ Luxembourg                                               │ Onsite        │
│ Luxembourg                                               │ Onsite        │
│ San Salvador, El Salvador                                │ Onsite        │
│ Abidjan, Côte d’Ivoire                                   │ Onsite        │
│ Anywhere                                                 │ Remote        │
│ Internatsionalnaya, Kyrgyzstan                           │ Onsite        │
│ Anywhere                                                 │ Remote        │
└──────────────────────────────────────────────────────────┴───────────────┘
*/

--- SECTION 8: DATA CLEANING

---QUESTION #29
---Return job_title and a cleaned version called clean_job_title.
---The cleaned version should be lowercase and trimmed.
SELECT
    job_title,
    LOWER(TRIM(job_title)) AS clean_job_title
FROM
    job_postings_fact;
/*
┌────────────────────────────────────────────┬────────────────────────────────────────────┐
│                 job_title                  │              clean_job_title               │
│                  varchar                   │                  varchar                   │
├────────────────────────────────────────────┼────────────────────────────────────────────┤
│ Data Analyst                               │ data analyst                               │
│ Data Analyst                               │ data analyst                               │
│ Data Analyst                               │ data analyst                               │
│ Senior Data Analyst / Platform Experience  │ senior data analyst / platform experience  │
│ Data Analyst                               │ data analyst                               │
│ Jr. Data Analyst                           │ jr. data analyst                           │
│ Data Analyst                               │ data analyst                               │
│ Loyalty Data Analyst III                   │ loyalty data analyst iii                   │
│ Senior data analyst                        │ senior data analyst                        │
│ Business Analyst - Taxonomy/Ontology       │ business analyst - taxonomy/ontology       │
│ Technical Data Analyst / Designer -- 2207… │ technical data analyst / designer -- 2207… │
│ Neuroscience Research Data Analyst         │ neuroscience research data analyst         │
│ Data Analyst                               │ data analyst                               │
│ BI Data Analyst                            │ bi data analyst                            │
│ EDI Data Analyst                           │ edi data analyst                           │
│ Data Analyst for Member Contact Center     │ data analyst for member contact center     │
│ BI Data Analyst                            │ bi data analyst                            │
│ Data Analyst, Partner Operations (Ecosyst… │ data analyst, partner operations (ecosyst… │
│ Guidewire Policy Data Analyst              │ guidewire policy data analyst              │
│ Sr. Data Analyst                           │ sr. data analyst                           │
│        ·                                   │        ·                                   │
│        ·                                   │        ·                                   │
│        ·                                   │        ·                                   │
│ Full Stack .NET Developer (For MediaSoft … │ full stack .net developer (for mediasoft … │
│ Knowledge Graph Data Engineer              │ knowledge graph data engineer              │
│ Data Software Engineer                     │ data software engineer                     │
│ Data Engineer                              │ data engineer                              │
│ Data Scientist - QuantumBlack, AI by McKi… │ data scientist - quantumblack, ai by mcki… │
│ Data Engineer I                            │ data engineer i                            │
│ Senior Data Scientist                      │ senior data scientist                      │
│ Data Engineer                              │ data engineer                              │
│ Principal Software Engineer                │ principal software engineer                │
│ Data Analyst                               │ data analyst                               │
│ Data Analyst/ Compliance Analytics & Moni… │ data analyst/ compliance analytics & moni… │
│ Data Analyst                               │ data analyst                               │
│ Systems Assurance and Data Analytics Engi… │ systems assurance and data analytics engi… │
│ Senior Data Scientist                      │ senior data scientist                      │
│ Data Science Manager                       │ data science manager                       │
│ Tutor-Reviewer For Data Science Program    │ tutor-reviewer for data science program    │
│ DATA ENGINEER                              │ data engineer                              │
│ Data Analyst - Moldova                     │ data analyst - moldova                     │
│ Junior Data Analyst / Developer, Nature f… │ junior data analyst / developer, nature f… │
│ Principal Data Scientist- Entity/ID Resol… │ principal data scientist- entity/id resol… │
└────────────────────────────────────────────┴────────────────────────────────────────────┘
*/

---QUESTION #30
---Return company_id, name, and clean_company_name.
---clean_company_name should trim spaces, convert to lowercase, and replace null with 'Unknown Company'.
SELECT
    company_id,
    name,
    LOWER(TRIM(COALESCE(name, 'Unknown Company'))) AS clean_company_name
FROM
    company_dim;
/*
┌────────────┬──────────────────────────────────────┬─────────────────────────────────────┐
│ company_id │                 name                 │         clean_company_name          │
│   int32    │               varchar                │               varchar               │
├────────────┼──────────────────────────────────────┼─────────────────────────────────────┤
│       4593 │ Metasys Technologies                 │ metasys technologies                │
│       4594 │ Guidehouse                           │ guidehouse                          │
│       4595 │ Protask                              │ protask                             │
│       4596 │ Atria Wealth Solutions               │ atria wealth solutions              │
│       4597 │ ICONMA, LLC                          │ iconma, llc                         │
│       4598 │ Aquent                               │ aquent                              │
│       4599 │ Adyen                                │ adyen                               │
│       4600 │ Albertsons Companies                 │ albertsons companies                │
│       4601 │ Panda Restaurant Group               │ panda restaurant group              │
│       4602 │ Diverse Lynx                         │ diverse lynx                        │
│       4603 │ Range Generation Next LLC            │ range generation next llc           │
│       4604 │ Stanford University Lee Lab          │ stanford university lee lab         │
│       4605 │ CYNET SYSTEMS                        │ cynet systems                       │
│       4606 │ Trident Consulting                   │ trident consulting                  │
│       4607 │ EDI Staffing                         │ edi staffing                        │
│       4608 │ Workway                              │ workway                             │
│       4609 │ Omega Solutions                      │ omega solutions                     │
│       4610 │ ByteDance                            │ bytedance                           │
│       4611 │ Tekfortune Inc.                      │ tekfortune inc.                     │
│       4612 │ VLink Inc.                           │ vlink inc.                          │
│         ·  │     ·                                │     ·                               │
│         ·  │     ·                                │     ·                               │
│         ·  │     ·                                │     ·                               │
│    1620348 │ Net4market - CSAmed                  │ net4market - csamed                 │
│    1620353 │ beBeeComputerScience                 │ bebeecomputerscience                │
│    1620355 │ beBeeActuary                         │ bebeeactuary                        │
│    1620357 │ Accusaga Inc                         │ accusaga inc                        │
│    1620364 │ beBeeInnovazione                     │ bebeeinnovazione                    │
│    1620365 │ beBeeCARRIERE                        │ bebeecarriere                       │
│    1620368 │ HÖEGH LNG SERVICES ROHQ              │ höegh lng services rohq             │
│    1620376 │ Agilent Diagnostics & Genomics Solu… │ agilent diagnostics & genomics sol… │
│    1620382 │ Edgecortix                           │ edgecortix                          │
│    1620384 │ Empathy Nails                        │ empathy nails                       │
│    1620385 │ MD_HCHN Holy Cross Health, Inc.      │ md_hchn holy cross health, inc.     │
│    1620388 │ EMCOR Group Inc.                     │ emcor group inc.                    │
│    1620399 │ Healing Hands Ministries Inc         │ healing hands ministries inc        │
│    1620419 │ QA USA, Inc.                         │ qa usa, inc.                        │
│    1620432 │ beBeeFinancialAccountant             │ bebeefinancialaccountant            │
│    1620443 │ beBeeWorkday                         │ bebeeworkday                        │
│    1620447 │ Bedrock Security                     │ bedrock security                    │
│    1620479 │ beBeeDataScienceEngineer             │ bebeedatascienceengineer            │
│    1620495 │ Hariphil Asia Resources, Inc.        │ hariphil asia resources, inc.       │
│    1620514 │ Make (make.com)                      │ make (make.com)                     │
└────────────┴──────────────────────────────────────┴─────────────────────────────────────┘
*/

---QUESTION #31 TRIM/COAELSCE/CASE
---Clean job_location by trimming spaces.
---If the trimmed value is blank or null, return 'Unknown'.
---Return it as clean_job_location.
SELECT
   CASE
        WHEN job_location IS NULL OR TRIM(job_location) = '' THEN 'Unknown'
        ELSE TRIM(job_location)
   END AS clean_job_location
FROM
    job_postings_fact;
/*
┌──────────────────────────────────────────────────────────┐
│                    clean_job_location                    │
│                         varchar                          │
├──────────────────────────────────────────────────────────┤
│ New York, NY                                             │
│ Washington, DC                                           │
│ Fairfax, VA                                              │
│ Worcester, MA                                            │
│ Sunnyvale, CA                                            │
│ Torrance, CA                                             │
│ San Francisco, CA                                        │
│ Pleasanton, CA                                           │
│ Rosemead, CA                                             │
│ Thousand Oaks, CA                                        │
│ Vandenberg AFB, CA                                       │
│ Stanford, CA                                             │
│ Irvine, CA                                               │
│ San Jose, CA                                             │
│ Fullerton, CA                                            │
│ Pasadena, CA                                             │
│ Santa Clara, CA                                          │
│ San Francisco, CA                                        │
│ Sunnyvale, CA                                            │
│ Los Angeles, CA                                          │
│        ·                                                 │
│        ·                                                 │
│        ·                                                 │
│ Dhaka, Bangladesh                                        │
│ Casalecchio di Reno, Metropolitan City of Bologna, Italy │
│ Milan, Metropolitan City of Milan, Italy                 │
│ Fes, Morocco                                             │
│ Madrid, Spain                                            │
│ Sri Lanka                                                │
│ Anywhere                                                 │
│ Moscow, Russia                                           │
│ Nepal                                                    │
│ Prague, Czechia                                          │
│ Prague, Czechia                                          │
│ Olomouc, Czechia                                         │
│ Dar es Salaam, Tanzania                                  │
│ Luxembourg                                               │
│ Luxembourg                                               │
│ San Salvador, El Salvador                                │
│ Abidjan, Côte d’Ivoire                                   │
│ Anywhere                                                 │
│ Internatsionalnaya, Kyrgyzstan                           │
│ Anywhere                                                 │
└──────────────────────────────────────────────────────────┘
*/

---QUESTION #32
---Find rows where job_title, company name, or job_location has leading or trailing spaces.
---Return the original values and cleaned values.
SELECT
    jpf.job_title AS original_job_title,
    TRIM(jpf.job_title) AS cleaned_job_title,

    cd.name AS original_company_name,
    TRIM(cd.name) cleaned_company_name,

    jpf.job_location AS original_job_location,
    TRIM(jpf.job_location) AS cleaned_job_location
FROM
    job_postings_fact AS jpf
JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id
WHERE
    (jpf.job_title LIKE ' %' OR jpf.job_title LIKE '% ')
    OR (cd.name LIKE ' %' OR cd.name LIKE '% ')
    OR (jpf.job_location LIKE ' %' OR jpf.job_location LIKE '% ');
/*
┌─────────────────────────────┬──────────────────────┬───┬──────────────────────┬──────────────────────┐
│     original_job_title      │  cleaned_job_title   │ … │ original_job_locati… │ cleaned_job_location │
│           varchar           │       varchar        │ … │       varchar        │       varchar        │
├─────────────────────────────┼──────────────────────┼───┼──────────────────────┼──────────────────────┤
│ Data Engineer               │ Data Engineer        │ … │ Belarus              │ Belarus              │
│ Data Engineer               │ Data Engineer        │ … │ Belarus              │ Belarus              │
│ Data Engineer with QE expe… │ Data Engineer with … │ … │ Fremont, CA          │ Fremont, CA          │
│ Data Engineer               │ Data Engineer        │ … │ Fremont, CA          │ Fremont, CA          │
│  GenAI Data Scientist       │ GenAI Data Scientist │ … │ Washington, DC       │ Washington, DC       │
│ Big Data Engineer           │ Big Data Engineer    │ … │ United States        │ United States        │
│  GCP Data Engineer          │ GCP Data Engineer    │ … │ Richardson, TX       │ Richardson, TX       │
│ Data Engineer               │ Data Engineer        │ … │ Fremont, CA          │ Fremont, CA          │
│ Data Analyst                │ Data Analyst         │ … │ Austin, TX           │ Austin, TX           │
│  Celonis Data Engineer      │ Celonis Data Engine… │ … │ Wayzata, MN          │ Wayzata, MN          │
│ Senior Data Analyst         │ Senior Data Analyst  │ … │ Fremont, CA          │ Fremont, CA          │
│ Role: Data Engineer         │ Role: Data Engineer  │ … │ Fremont, CA          │ Fremont, CA          │
│ Data Engineer Spark + Scal… │ Data Engineer Spark… │ … │ Austin, TX           │ Austin, TX           │
│ Data Engineer               │ Data Engineer        │ … │ Austin, TX           │ Austin, TX           │
│ Data Engineer               │ Data Engineer        │ … │ Plano, TX            │ Plano, TX            │
│  Splunk Business Analyst    │ Splunk Business Ana… │ … │ Irving, TX           │ Irving, TX           │
│ Senior Data Scientist     … │ Senior Data Scienti… │ … │ Alpharetta, GA       │ Alpharetta, GA       │
│ Snowflake Data Engineer     │ Snowflake Data Engi… │ … │ Dallas, TX           │ Dallas, TX           │
│ Data scientist              │ Data scientist       │ … │ Belarus              │ Belarus              │
│  Data and Reporting Analyst │ Data and Reporting … │ … │ Reston, VA           │ Reston, VA           │
│ Data Architect with Data E… │ Data Architect with… │ … │ Dallas, TX           │ Dallas, TX           │
│ Data Scientist              │ Data Scientist       │ … │ Atlanta, GA          │ Atlanta, GA          │
│ Cloud data scientist        │ Cloud data scientist │ … │ Belarus              │ Belarus              │
│ Data Engineer               │ Data Engineer        │ … │ Belarus              │ Belarus              │
│ Digital Marketer            │ Digital Marketer     │ … │ Belarus              │ Belarus              │
│ Big Data Engineer           │ Big Data Engineer    │ … │ Belarus              │ Belarus              │
│ Middle Java Software Engin… │ Middle Java Softwar… │ … │ Belarus              │ Belarus              │
│ Data Scientist              │ Data Scientist       │ … │ Dubai - United Arab… │ Dubai - United Arab… │
│ Mission Data Engineer H/F … │ Mission Data Engine… │ … │ Paris, France        │ Paris, France        │
│ Data Engineer               │ Data Engineer        │ … │ Indianapolis, IN     │ Indianapolis, IN     │
│ Lead Engineer - Kubernetes… │ Lead Engineer - Kub… │ … │ United Kingdom       │ United Kingdom       │
│ Technical Support Engineer… │ Technical Support E… │ … │ Tel Aviv-Yafo, Isra… │ Tel Aviv-Yafo, Isra… │
│  Staff, Data Scientist (SC… │ Staff, Data Scienti… │ … │ Seoul, South Korea   │ Seoul, South Korea   │
│ Big Data Engineer           │ Big Data Engineer    │ … │ Belarus              │ Belarus              │
│ Machine Learning Engineer   │ Machine Learning En… │ … │ Anywhere             │ Anywhere             │
│ Data scientist              │ Data scientist       │ … │ Belarus              │ Belarus              │
└─────────────────────────────┴──────────────────────┴───┴──────────────────────┴──────────────────────┘
*/

--- SECTION 9: DATA QUALITY CHECKS

---QUESTION #33
---Count total rows in job_postings_fact.
---Also count missing salaries, missing locations, and missing company_id values.
SELECT
    COUNT(*) total_rows,
    COUNT(*) - COUNT(salary_year_avg) AS missing_salaries,
    COUNT(*) - COUNT(job_location) AS missing_locations,
    COUNT(*) - COUNT(company_id) AS missing_company_id
FROM 
    job_postings_fact;
/*
┌────────────┬──────────────────┬───────────────────┬────────────────────┐
│ total_rows │ missing_salaries │ missing_locations │ missing_company_id │
│   int64    │      int64       │       int64       │       int64        │
├────────────┼──────────────────┼───────────────────┼────────────────────┤
│    1615930 │          1564904 │              3528 │                  0 │
└────────────┴──────────────────┴───────────────────┴────────────────────┘
*/

---QUESTION #34
---Check whether job_id has duplicates.
---Return job_id and duplicate_count.
---Only show job_id values where duplicate_count > 1.
SELECT
    job_id,
    COUNT(*) AS duplicate_count
FROM
    job_postings_fact
GROUP BY 
    job_id
HAVING
    duplicate_count > 1;
/*
┌────────┬─────────────────┐
│ job_id │ duplicate_count │
│ int32  │      int64      │
└────────┴─────────────────┘
*/

---QUESTION #35
---Check for possible duplicate job postings using:
---company_id, job_title_short, job_title, job_location, and salary_year_avg.
---Return those columns and duplicate_count.
---Only show duplicates.
SELECT
    job_title_short,
    company_id,
    job_title,
    job_location,
    salary_year_avg,
    COUNT(*) AS duplicate_count
FROM
    job_postings_fact
WHERE
    salary_year_avg IS NOT NULL
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
/*
┌───────────────────────────┬────────────┬───┬─────────────────┬─────────────────┐
│      job_title_short      │ company_id │ … │ salary_year_avg │ duplicate_count │
│          varchar          │   int32    │ … │     double      │      int64      │
├───────────────────────────┼────────────┼───┼─────────────────┼─────────────────┤
│ Machine Learning Engineer │       4765 │ … │         65000.0 │              63 │
│ Senior Data Analyst       │       4695 │ … │        148000.0 │              63 │
│ Business Analyst          │     101973 │ … │         87000.0 │              63 │
│ Data Scientist            │     143071 │ … │        120000.0 │              63 │
│ Data Analyst              │       4641 │ … │        100000.0 │              63 │
│ Data Engineer             │      64978 │ … │        160000.0 │              63 │
│ Data Scientist            │       7188 │ … │        125000.0 │              63 │
│ Data Analyst              │     873351 │ … │         79000.0 │              63 │
│ Data Scientist            │     325053 │ … │         75000.0 │              63 │
│ Data Scientist            │      10350 │ … │        120000.0 │              63 │
│ Senior Data Scientist     │      22171 │ … │        169500.0 │              63 │
│ Senior Data Engineer      │       9912 │ … │        221844.0 │              63 │
│ Software Engineer         │       6548 │ … │        190000.0 │              62 │
│ Data Scientist            │     690941 │ … │         90000.0 │              62 │
│ Data Analyst              │     873351 │ … │         77000.0 │              62 │
│ Data Engineer             │     698606 │ … │        157500.0 │              62 │
│ Data Analyst              │     873351 │ … │         94455.0 │              62 │
│ Data Engineer             │      33906 │ … │        200000.0 │              61 │
│ Senior Data Analyst       │     542180 │ … │        110000.0 │              60 │
│ Data Engineer             │       7013 │ … │        162500.0 │              59 │
│       ·                   │         ·  │ … │               · │               · │
│       ·                   │         ·  │ … │               · │               · │
│       ·                   │         ·  │ … │               · │               · │
│ Data Engineer             │     324715 │ … │        228060.0 │               2 │
│ Data Engineer             │      14837 │ … │        122500.0 │               2 │
│ Data Scientist            │    1557706 │ … │        156500.0 │               2 │
│ Data Analyst              │     324715 │ … │         95000.0 │               2 │
│ Data Analyst              │    1606004 │ … │         52500.0 │               2 │
│ Data Scientist            │      21574 │ … │        130000.0 │               2 │
│ Data Scientist            │     419422 │ … │        142000.0 │               2 │
│ Data Scientist            │       4867 │ … │        175000.0 │               2 │
│ Data Scientist            │     355838 │ … │        147500.0 │               2 │
│ Data Scientist            │      12557 │ … │        104650.0 │               2 │
│ Data Engineer             │       6898 │ … │        237000.0 │               2 │
│ Senior Data Analyst       │       4830 │ … │        108267.0 │               2 │
│ Senior Data Engineer      │     154155 │ … │        102500.0 │               2 │
│ Business Analyst          │     321119 │ … │        110000.0 │               2 │
│ Data Engineer             │    1218887 │ … │        124753.5 │               2 │
│ Data Analyst              │       6069 │ … │         95680.0 │               2 │
│ Data Analyst              │       6069 │ … │         85000.0 │               2 │
│ Machine Learning Engineer │      23605 │ … │        185500.0 │               2 │
│ Data Scientist            │      75000 │ … │        130000.0 │               2 │
│ Data Analyst              │       9298 │ … │         78740.0 │               2 │
└───────────────────────────┴────────────┴───┴─────────────────┴─────────────────┘
*/

---QUESTION #36
---Count total jobs, jobs with a valid company match, and jobs with a missing company reference.
---Use a LEFT JOIN between job_postings_fact and company_dim.
SELECT
    COUNT(*) AS total_jobs,
    COUNT(cd.company_id) AS jobs_with_valid_company_match,
    COUNT(*) - COUNT(cd.company_id) AS jobs_with_missing_company_reference
FROM
    job_postings_fact AS jpf
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id;
/*
┌────────────┬───────────────────────────────┬─────────────────────────────────┐
│ total_jobs │ jobs_with_valid_company_match │ jobs_with_missing_company_refer │
│            │                               │              ence               │
│   int64    │             int64             │              int64              │
├────────────┼───────────────────────────────┼─────────────────────────────────┤
│    1615930 │                       1615930 │                               0 │
└────────────┴───────────────────────────────┴─────────────────────────────────┘
*/

--- SECTION 10: DATE AND LAG

---QUESTION #37
---Count jobs posted per day using DATE_TRUNC('day', job_posted_date).
---Return posted_day and total_jobs.
---Order by posted_day.
SELECT
    COUNT(job_id) AS tOtal_jobs,
    DATE_TRUNC('day', job_posted_date) AS posted_day
FROM
    job_postings_fact
GROUP BY 
    posted_day;
/*
┌────────────┬─────────────────────┐
│ tOtal_jobs │     posted_day      │
│   int64    │      timestamp      │
├────────────┼─────────────────────┤
│       1556 │ 2023-05-07 00:00:00 │
│       2775 │ 2024-02-27 00:00:00 │
│       2147 │ 2024-02-29 00:00:00 │
│       2027 │ 2024-03-05 00:00:00 │
│        968 │ 2024-03-16 00:00:00 │
│       2743 │ 2023-10-04 00:00:00 │
│       2643 │ 2023-10-10 00:00:00 │
│       2566 │ 2023-11-07 00:00:00 │
│       2222 │ 2023-11-13 00:00:00 │
│       1799 │ 2023-02-04 00:00:00 │
│       2527 │ 2023-02-10 00:00:00 │
│       1936 │ 2025-03-05 00:00:00 │
│       2144 │ 2025-03-09 00:00:00 │
│        851 │ 2024-06-08 00:00:00 │
│       1766 │ 2024-06-13 00:00:00 │
│        845 │ 2024-06-15 00:00:00 │
│       1749 │ 2024-06-25 00:00:00 │
│        853 │ 2024-07-21 00:00:00 │
│       2005 │ 2024-08-09 00:00:00 │
│       3620 │ 2025-02-02 00:00:00 │
│         ·  │          ·          │
│         ·  │          ·          │
│         ·  │          ·          │
│       2173 │ 2024-01-02 00:00:00 │
│       1069 │ 2024-01-06 00:00:00 │
│       1082 │ 2024-01-13 00:00:00 │
│       1234 │ 2025-04-08 00:00:00 │
│       1947 │ 2025-05-07 00:00:00 │
│       1522 │ 2025-05-08 00:00:00 │
│       1624 │ 2025-05-20 00:00:00 │
│       1202 │ 2025-05-21 00:00:00 │
│       1184 │ 2025-05-23 00:00:00 │
│       1478 │ 2025-06-03 00:00:00 │
│       1264 │ 2025-06-18 00:00:00 │
│       2453 │ 2023-02-21 00:00:00 │
│       1460 │ 2023-03-05 00:00:00 │
│       2158 │ 2023-04-06 00:00:00 │
│       1813 │ 2024-03-22 00:00:00 │
│        633 │ 2024-03-24 00:00:00 │
│       1869 │ 2024-04-08 00:00:00 │
│       1456 │ 2024-04-24 00:00:00 │
│       1874 │ 2024-05-10 00:00:00 │
│       1572 │ 2024-05-16 00:00:00 │
└────────────┴─────────────────────┘
*/

---QUESTION #38
---Using the daily job counts from question #37, add previous_day_jobs.
---Use LAG(total_jobs) ordered by posted_day.
WITH daily_job AS (
    SELECT
        DATE_TRUNC('day', job_posted_date) AS posted_day,
        COUNT(*) AS total_jobs
    FROM
        job_postings_fact
    GROUP BY
        posted_day
)
SELECT
    posted_day,
    total_jobs,
    LAG(total_jobs) OVER(
        ORDER BY posted_day
    ) AS previous_day_jobs
FROM
    daily_job
ORDER BY
    posted_day;
/*
┌─────────────────────┬────────────┬───────────────────┐
│     posted_day      │ total_jobs │ previous_day_jobs │
│      timestamp      │   int64    │       int64       │
├─────────────────────┼────────────┼───────────────────┤
│ 2023-01-01 00:00:00 │       3581 │              NULL │
│ 2023-01-02 00:00:00 │       2737 │              3581 │
│ 2023-01-03 00:00:00 │       2564 │              2737 │
│ 2023-01-04 00:00:00 │       3967 │              2564 │
│ 2023-01-05 00:00:00 │       3305 │              3967 │
│ 2023-01-06 00:00:00 │       3337 │              3305 │
│ 2023-01-07 00:00:00 │       2077 │              3337 │
│ 2023-01-08 00:00:00 │       2312 │              2077 │
│ 2023-01-09 00:00:00 │       2737 │              2312 │
│ 2023-01-10 00:00:00 │       3358 │              2737 │
│ 2023-01-11 00:00:00 │       3387 │              3358 │
│ 2023-01-12 00:00:00 │       3300 │              3387 │
│ 2023-01-13 00:00:00 │       3125 │              3300 │
│ 2023-01-14 00:00:00 │       2832 │              3125 │
│ 2023-01-15 00:00:00 │       2304 │              2832 │
│ 2023-01-16 00:00:00 │       2869 │              2304 │
│ 2023-01-17 00:00:00 │       2919 │              2869 │
│ 2023-01-18 00:00:00 │       3113 │              2919 │
│ 2023-01-19 00:00:00 │       3239 │              3113 │
│ 2023-01-20 00:00:00 │       3684 │              3239 │
│          ·          │         ·  │                ·  │
│          ·          │         ·  │                ·  │
│          ·          │         ·  │                ·  │
│ 2025-06-11 00:00:00 │       1270 │              1452 │
│ 2025-06-12 00:00:00 │       1290 │              1270 │
│ 2025-06-13 00:00:00 │       1204 │              1290 │
│ 2025-06-14 00:00:00 │        920 │              1204 │
│ 2025-06-15 00:00:00 │       1009 │               920 │
│ 2025-06-16 00:00:00 │       1112 │              1009 │
│ 2025-06-17 00:00:00 │       1371 │              1112 │
│ 2025-06-18 00:00:00 │       1264 │              1371 │
│ 2025-06-19 00:00:00 │       1048 │              1264 │
│ 2025-06-20 00:00:00 │       1218 │              1048 │
│ 2025-06-21 00:00:00 │        915 │              1218 │
│ 2025-06-22 00:00:00 │        706 │               915 │
│ 2025-06-23 00:00:00 │       1187 │               706 │
│ 2025-06-24 00:00:00 │       1253 │              1187 │
│ 2025-06-25 00:00:00 │       1084 │              1253 │
│ 2025-06-26 00:00:00 │       1373 │              1084 │
│ 2025-06-27 00:00:00 │       1236 │              1373 │
│ 2025-06-28 00:00:00 │       1014 │              1236 │
│ 2025-06-29 00:00:00 │        854 │              1014 │
│ 2025-06-30 00:00:00 │        138 │               854 │
└─────────────────────┴────────────┴───────────────────┘
*/

--- SECTION 11: CHALLENGE QUESTIONS

---QUESTION #39
---Find the top 10 job_title_short roles by remote job percentage.
---Return job_title_short, total_jobs, remote_jobs, and remote_percentage.
---Order by remote_percentage descending.
SELECT
    job_title_short,
    COUNT(*) AS total_jobs,
    SUM(
        CASE
            WHEN job_work_from_home = TRUE THEN 1
            ELSE 0
        END
    ) AS remote_jobs,
        ROUND(
            SUM(
            CASE
                WHEN job_work_from_home = TRUE THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2 
    ) AS remote_percantage
FROM
    job_postings_fact
GROUP BY
    job_title_short
ORDER BY
    remote_percantage  DESC;
/*
┌────────────┬───────────────────────────┬─────────────┬───────────────────┐
│ total_jobs │      job_title_short      │ remote_jobs │ remote_percantage │
│   int64    │          varchar          │   int128    │      double       │
├────────────┼───────────────────────────┼─────────────┼───────────────────┤
│      91295 │ Senior Data Engineer      │       13115 │             14.37 │
│     391957 │ Data Engineer             │       43853 │             11.19 │
│      39628 │ Machine Learning Engineer │        4416 │             11.14 │
│      70877 │ Senior Data Scientist     │        7403 │             10.44 │
│     331002 │ Data Scientist            │       29331 │              8.86 │
│      59383 │ Senior Data Analyst       │        4709 │              7.93 │
│      92271 │ Software Engineer         │        6980 │              7.56 │
│     408640 │ Data Analyst              │       27185 │              6.65 │
│     101167 │ Business Analyst          │        6218 │              6.15 │
│      29710 │ Cloud Engineer            │        1322 │              4.45 │
└────────────┴───────────────────────────┴─────────────┴───────────────────┘
*/

---QUESTION #40
---For each job_title_short, find the skill with the highest demand_count.
---Return job_title_short, skill_name, demand_count, and skill_rank.
---Use a CTE and ROW_NUMBER().
WITH rank_num AS (
    SELECT
        job_title_short,
        sd.skills AS skill_name,
        COUNT(*) AS demand_count,
        ROW_NUMBER() OVER(
            PARTITION BY job_title_short
            ORDER BY demand_count DESC
        ) AS skill_rank
    FROM
        job_postings_fact AS jpf
    JOIN skills_job_dim AS sjd
        ON jpf.job_id = sjd.job_id
    JOIN skills_dim AS sd
        ON sjd.skill_id = sd.skill_id
    GROUP BY 
        job_title_short,
        skill_name
    ORDER BY
        demand_count DESC
)
SELECT
    job_title_short,
    skill_name,
    demand_count,
    skill_rank
FROM
    rank_num;

