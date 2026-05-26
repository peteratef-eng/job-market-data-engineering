/*
SQL REVIEW QUESTIONS

Write your answers under each question.
Use the same tables you practiced with:
- job_postings_fact
- company_dim
- skills_job_dim
- skills_dim
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



--- SECTION 6: WINDOW FUNCTIONS

---QUESTION #19
---For each job row with a salary, show:
---job_id, job_title_short, salary_year_avg, and avg_salary_for_title.
---Use AVG() OVER(PARTITION BY job_title_short).



---QUESTION #20
---Find the highest salary job for each job_title_short.
---Use ROW_NUMBER() with PARTITION BY job_title_short.
---Return job_title_short, job_id, salary_year_avg, and salary_rank.



---QUESTION #21
---Find the top 3 salaries for each job_title_short.
---Use ROW_NUMBER() with PARTITION BY job_title_short.
---Only include rows where salary_year_avg is not null.



---QUESTION #22
---Find the lowest salary for each job_title_short.
---Use ROW_NUMBER() ordered by salary_year_avg ascending.



---QUESTION #23
---Use RANK() to rank salaries within each job_title_short.
---Return job_title_short, salary_year_avg, and rank_num.
---Order salaries from highest to lowest inside each job title.



---QUESTION #24
---Use DENSE_RANK() to rank salaries within each job_title_short.
---Return job_title_short, salary_year_avg, and dense_rank.
---Order salaries from highest to lowest inside each job title.



---QUESTION #25
---Calculate a running total of salary_year_avg within each job_title_short.
---Use SUM() OVER(PARTITION BY job_title_short ORDER BY salary_year_avg).
---Only include rows where salary_year_avg is not null.



---QUESTION #26
---Calculate the percentage of each job_title_short compared to total jobs.
---Return job_title_short, total_jobs_by_title, total_jobs, and job_title_percentage.
---Use COUNT(*) and a window function.
---Order by job_title_percentage descending.



--- SECTION 7: CASE WHEN

---QUESTION #27
---Create a salary_category column:
---High Salary if salary_year_avg >= 150000
---Medium Salary if salary_year_avg >= 80000
---Low Salary otherwise
---Only include rows where salary_year_avg is not null.



---QUESTION #28
---Create a remote_status column:
---Remote if job_location is 'Anywhere'
---Onsite if job_location is not 'Anywhere'
---Unknown if job_location is null or blank.



--- SECTION 8: DATA CLEANING

---QUESTION #29
---Return job_title and a cleaned version called clean_job_title.
---The cleaned version should be lowercase and trimmed.



---QUESTION #30
---Return company_id, name, and clean_company_name.
---clean_company_name should trim spaces, convert to lowercase, and replace null with 'Unknown Company'.



---QUESTION #31
---Clean job_location by trimming spaces.
---If the trimmed value is blank or null, return 'Unknown'.
---Return it as clean_job_location.



---QUESTION #32
---Find rows where job_title, company name, or job_location has leading or trailing spaces.
---Return the original values and cleaned values.



--- SECTION 9: DATA QUALITY CHECKS

---QUESTION #33
---Count total rows in job_postings_fact.
---Also count missing salaries, missing locations, and missing company_id values.



---QUESTION #34
---Check whether job_id has duplicates.
---Return job_id and duplicate_count.
---Only show job_id values where duplicate_count > 1.



---QUESTION #35
---Check for possible duplicate job postings using:
---company_id, job_title_short, job_title, job_location, and salary_year_avg.
---Return those columns and duplicate_count.
---Only show duplicates.



---QUESTION #36
---Count total jobs, jobs with a valid company match, and jobs with a missing company reference.
---Use a LEFT JOIN between job_postings_fact and company_dim.



--- SECTION 10: DATE AND LAG

---QUESTION #37
---Count jobs posted per day using DATE_TRUNC('day', job_posted_date).
---Return posted_day and total_jobs.
---Order by posted_day.



---QUESTION #38
---Using the daily job counts from question #37, add previous_day_jobs.
---Use LAG(total_jobs) ordered by posted_day.



--- SECTION 11: CHALLENGE QUESTIONS

---QUESTION #39
---Find the top 10 job_title_short roles by remote job percentage.
---Return job_title_short, total_jobs, remote_jobs, and remote_percentage.
---Order by remote_percentage descending.



---QUESTION #40
---For each job_title_short, find the skill with the highest demand_count.
---Return job_title_short, skill_name, demand_count, and skill_rank.
---Use a CTE and ROW_NUMBER().


