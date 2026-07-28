# Market Dashboard Data and Analytics Validation Audit

Scope: read-only audit of `data/dashboard/jobs_sample.csv`, `data/dashboard/job_skills_sample.csv`, `data/dashboard/metadata.json`, `views/market_dashboard.py`, `dashboard/data_loader.py`, `dashboard/transformations.py`, `dashboard/charts.py`, and `scripts/prepare_dashboard_data.py`.

No production dashboard code or production data was modified during this audit.

## Summary Table

| Check | Expected | Actual | Status | Evidence |
| ----- | -------: | -----: | ------ | -------- |
| Hosted job sample rows | 150,000 | 150,000 | PASS | `len(jobs_sample.csv)` via `load_dashboard_data()` |
| Hosted job-skills rows | 667,829 | 667,829 | PASS | `len(job_skills_sample.csv)` and `metadata.sample_job_skills_rows` |
| Source posting total | 1,615,930 | 1,615,930 | PASS | Independently counted `data/job_postings_fact.csv` |
| Sample reproducibility | 150,000 matching random-state job IDs | 150,000 matching IDs | PASS | Raw `job_postings_fact.csv.sample(n=150000, random_state=42)` exactly matched hosted job IDs |
| Job columns | 11 expected dashboard columns | 11 present | PASS | `dashboard/data_loader.py` typed read |
| Skill columns | 4 expected dashboard columns | 4 present | PASS | `dashboard/data_loader.py` typed read |
| Missing job IDs | 0 | 0 | PASS | `jobs["job_id"].isna().sum()` |
| Missing skill job IDs | 0 | 0 | PASS | `skills["job_id"].isna().sum()` |
| Duplicate job IDs | 0 | 0 | PASS | `jobs["job_id"].duplicated().sum()` |
| Duplicate full job rows | 0 | 0 | PASS | `jobs.duplicated().sum()` |
| Duplicate full skill rows | 0 | 0 | PASS | `skills.duplicated().sum()` |
| Invalid parsed posting dates | 0 | 0 | PASS | `jobs["job_posted_date"].isna().sum()` |
| Posting date range | Valid min/max | 2023-01-01 00:01:15 to 2025-06-30 07:02:42 | PASS | Parsed datetime columns |
| Negative yearly salaries | 0 | 0 | PASS | `salary_year_avg < 0` |
| Implausible yearly salaries | 0 below 10,000 or above 1,000,000 | min 16,800; max 680,000 | PASS | Exploratory salary bounds |
| Completely empty columns | 0 | 0 | PASS | `isna().all()` |
| Empty key labels | 0 | 0 | PASS | job title, company, country, skill name stripped empty checks |
| Leading/trailing whitespace | 0 | 0 | PASS | All dashboard string columns checked with `str.strip()` |
| Remote-status categories | Onsite, Remote, Unknown | Onsite 136,147; Remote 13,524; Unknown 329 | PASS | `remote_status.value_counts()` |
| Orphan skill rows | 0 | 0 | PASS | Every skill `job_id` exists in jobs |
| Jobs without skills | Ideally documented if present | 26,501 | WARNING | These jobs contribute to posting KPIs/charts but not skill charts |
| Duplicate `(job_id, clean_skill_name)` relationships | 0 | 11,008 | FAIL | Duplicate cleaned names across different `skill_id` / type pairs |
| Duplicate `(job_id, skill_id)` relationships | 0 | 0 | PASS | Bridge-level skill IDs are unique per job |
| Join preserves job identity | 150,000 unique jobs after join | 150,000 unique jobs | PASS | Jobs-to-skills merge creates 694,330 rows but does not lose job IDs |
| Total postings KPI | Filtered job dataframe row count | 150.0K unfiltered | PASS | `kpi_values()` line 29 and independent formula |
| Company KPI | Distinct `company_id` | 54.9K | PASS | `company_id.nunique()` |
| Country KPI | Distinct non-null `job_country` | 161 | PASS | `job_country.dropna().nunique()` |
| Skill KPI | Distinct non-null `clean_skill_name` after filtering | 241 | PASS | `clean_skill_name.dropna().nunique()` |
| Average salary KPI | Mean non-null `salary_year_avg` before any job-skill join | $125,050 | PASS | 4,648 salary rows; nulls excluded |
| Median salary KPI | Median non-null `salary_year_avg` before any job-skill join | $119,257 | PASS | 4,648 salary rows; nulls excluded |
| Remote share KPI | Remote postings / all filtered postings, Unknown included in denominator | 9.0% | PASS | 13,524 / 150,000 |
| Salary coverage KPI | Valid yearly salary postings / total filtered postings | 3.1% | PASS | 4,648 / 150,000 |
| Filter operation within same filter | OR | OR | PASS | `.isin(...)` in `filter_jobs()` |
| Filter operation across filters | AND | AND | PASS | Sequential dataframe narrowing in `filter_jobs()` |
| Salary range filter behavior | Consistent with dashboard implementation | Includes null salaries plus in-range salaries | WARNING | `dashboard/data_loader.py` line 87 keeps `salary.isna()` rows |
| Empty-result handling | Stop before charts in page; helpers return empty tables | Works | PASS | Zero-record scenario and helper tests |
| Most In-Demand Job Titles | Counts filtered rows by `job_title_short`, top 15 | Matches independent table | PASS | `top_counts(filtered_jobs, "job_title_short")` |
| Most In-Demand Technical Skills | Unique job count by skill name and type, top 15 | Matches independent table | PASS | `top_skills(filtered_skills)` |
| Top Hiring Companies | Counts filtered rows by `clean_company_name`, top 15 | Matches independent table | PASS | `top_counts(filtered_jobs, "clean_company_name")` |
| Average Salary by Job Title | Mean salary by job title, salary rows only, min 3 jobs, top 15 | Matches independent table | PASS | `salary_by_dimension(..., "job_title_short")` |
| Average Salary by Country | Mean salary by country, salary rows only, min 3 jobs, top 15 | Matches independent table | PASS | `salary_by_dimension(..., "job_country")` |
| Remote vs On-site Salary | Mean salary by remote status, salary rows only | Matches independent table | PASS | `remote_salary(filtered_jobs)` |
| Job Posting Trends Over Time | Unique jobs by `posted_month`, chronological | Matches independent table | PASS | `monthly_trends(filtered_jobs)` |
| Monthly Job-Market Growth | Month-over-month percentage from monthly unique-job counts | Matches independent table | PASS | `monthly_trends(...).dropna(...)` in page |
| Skills Associated With Highest Salaries | Mean salary after skill join, min 3 unique jobs, top 15 | Matches independent table | PASS | `high_salary_skills(filtered_jobs, filtered_skills)` |
| Data Engineer Skill Demand | Unique job count by skill for filtered Data Engineer postings | Matches independent table | PASS | Data Engineer subset then `top_skills(...)` |
| Company category capitalization | No duplicate categories by case | 2,363 normalized-name variants | WARNING | Example: `2K` / `2k`, `3M` / `3m` |
| Chart axis labels | User-facing labels | User-facing labels present | PASS | `dashboard/charts.py` `LABELS` mapping |
| Cached results ignore filters | No cached filtered result | No cached filtered result | PASS | Only raw load is cached; filters are applied per rerun |
| Source total independently verifiable | Raw source available | Verified | PASS | Complete source CSV exists locally |

## Dataset Integrity

`jobs_sample.csv` contains 150,000 rows and 11 columns:

`job_id`, `company_id`, `job_title_short`, `clean_job_title`, `clean_job_location`, `job_country`, `remote_status`, `job_posted_date`, `posted_month`, `salary_year_avg`, `clean_company_name`.

`job_skills_sample.csv` contains 667,829 rows and 4 columns:

`job_id`, `skill_id`, `clean_skill_name`, `clean_skill_type`.

Loaded dtypes:

- Job IDs and company IDs: nullable integer.
- Job title, location, country, remote status, company, skill fields: pandas string.
- Posting dates and posted month: parsed datetimes.
- Salary: float.

Missing values:

- `salary_year_avg`: 145,352 missing values.
- All other dashboard columns: 0 missing values.

The large salary missingness is expected from the source sample and is handled by salary KPIs/charts by excluding null salary rows.

## Relationships

Every `job_id` in `job_skills_sample.csv` exists in `jobs_sample.csv`.

There are 26,501 jobs without skills. This is analytically acceptable if the dashboard intends total-posting KPIs and non-skill charts to include all postings, while skill charts include only postings with skill rows.

There are 11,008 duplicate `(job_id, clean_skill_name)` relationships. Examples show the same cleaned skill name attached to different `skill_id` / `clean_skill_type` values, such as:

- `sas` as both `programming` and `analyst_tools`
- `mongodb` as both `programming` and `databases`
- `firebase` as both `databases` and `cloud`

There are no duplicate `(job_id, skill_id)` relationships.

Failure detail:

- File: `scripts/prepare_dashboard_data.py`
- Function: `build_dashboard_dataset`
- Relevant line: 82
- Expected result: one `(job_id, clean_skill_name)` relationship if cleaned skill name is the semantic skill grain.
- Actual result: 11,008 duplicate cleaned skill-name relationships.
- Likely cause: source `skills_dim.csv` contains multiple `skill_id` values that clean to the same skill name under different skill types, and the preparation script writes the merged relationships without de-duplicating by cleaned skill name.
- Recommended correction: choose and document the intended skill grain. If skill name is the intended grain, de-duplicate by `(job_id, clean_skill_name)` during sample generation or canonicalize ambiguous skill IDs before exporting.

## KPIs

All KPI values matched independent Pandas calculations.

Formula definitions:

- Total postings: `len(filtered_jobs)`. This is equivalent to unique job count because `jobs_sample.csv` has no duplicate `job_id`.
- Companies: `filtered_jobs["company_id"].nunique()`.
- Countries: `filtered_jobs["job_country"].dropna().nunique()`.
- Skills: `filtered_skills["clean_skill_name"].dropna().nunique()`.
- Average yearly salary: mean of non-null `salary_year_avg` from filtered jobs only.
- Median yearly salary: median of non-null `salary_year_avg` from filtered jobs only.
- Remote share: `remote_status == "Remote"` divided by all filtered postings. `Unknown` is included in the denominator.
- Salary coverage: non-null `salary_year_avg` divided by all filtered postings.

Unfiltered KPI values:

- Total postings: 150.0K
- Companies: 54.9K
- Countries: 161
- Skills: 241
- Avg salary: $125,050
- Median salary: $119,257
- Remote share: 9.0%
- Salary coverage: 3.1%

## Filters

The filter implementation in `dashboard/data_loader.py` applies OR within each selected filter through `.isin(...)` and AND between filter categories through sequential narrowing.

Validated scenarios:

- No active filters: 150,000 jobs
- One job title (`Data Engineer`): 36,380 jobs
- Multiple job titles (`Data Analyst`, `Data Scientist`): 68,789 jobs
- One country (`United States`): 43,308 jobs
- One skill (`python`): 70,446 jobs
- Multiple skills (`python`, `sql`): 93,974 jobs
- One company: 57 jobs
- Multiple companies: 164 jobs
- Remote only: 13,524 jobs
- Onsite only: 136,147 jobs
- Combined work modes (`Remote`, `Onsite`): 149,671 jobs
- Narrow salary range: 145,745 jobs
- Narrow date range: 4,939 jobs
- Job title plus country: 8,270 jobs
- Skill plus work mode: 7,954 jobs
- Several filters simultaneously: 5,773 jobs
- Very few records: 2 jobs
- Zero records: 0 jobs
- Reset filters: 150,000 jobs

Warning: salary-range filtering keeps rows with null salary by design: `salary.isna() | salary.between(low, high)`. This preserves postings without salary data, but users may expect a salary range to exclude no-salary postings. This is behaviorally consistent across KPIs and charts.

## Charts

Every chart source table matched an independent calculation for categories, values, ordering, number of rows, top-N behavior, date grouping, percentage denominators, and null handling. Floating-point comparisons used `1e-9` absolute and relative tolerance.

Chart definitions:

- Most In-Demand Job Titles: `filtered_jobs`, group `job_title_short`, count rows, sort descending, top 15.
- Most In-Demand Technical Skills: `filtered_skills`, group `clean_skill_name` and `clean_skill_type`, count unique `job_id`, sort descending, top 15.
- Top Hiring Companies: `filtered_jobs`, group `clean_company_name`, count rows, sort descending, top 15.
- Average Salary by Job Title: filtered jobs with non-null salary, group `job_title_short`, mean and median salary, count unique `job_id`, require at least 3 salary jobs, sort mean descending, top 15.
- Average Salary by Country: filtered jobs with non-null salary, group `job_country`, mean and median salary, count unique `job_id`, require at least 3 salary jobs, sort mean descending, top 15.
- Remote vs On-site Salary: filtered jobs with non-null salary, group `remote_status`, mean salary and unique salary job count.
- Job Posting Trends Over Time: group filtered jobs by datetime `posted_month`, count unique `job_id`, sort chronologically.
- Monthly Job-Market Growth: same monthly table, percentage change from previous month; first month omitted by page before charting.
- Skills Associated With Highest Salaries: join filtered skill rows to filtered salary jobs, group by `clean_skill_name`, mean salary, count unique `job_id`, require at least 3 salary jobs, sort mean descending, top 15.
- Data Engineer Skill Demand: subset filtered jobs to `job_title_short == "Data Engineer"`, then group related skills by `clean_skill_name` and `clean_skill_type`, count unique `job_id`, sort descending, top 15.

Top unfiltered chart evidence:

- Job titles: Data Analyst 38,080; Data Engineer 36,380; Data Scientist 30,709.
- Skills: python 70,446; sql 70,274; aws 28,101.
- Companies: beBee Careers 2,994; Emprego 634; Capital One 611.
- Remote salary: Onsite $123,458 across 3,928 salary jobs; Remote $133,958 across 690 salary jobs; Unknown $128,534 across 30 salary jobs.

## Metadata Assertions

The metadata source total is independently verified because `data/job_postings_fact.csv` is present and contains 1,615,930 rows.

The hosted sample was also independently verified against the sample-generation script: sampling the raw source job file with `random_state=42` produced exactly the same 150,000 hosted job IDs.

## Risks and Discrepancies

1. FAIL: duplicate cleaned skill-name relationships.
   This is the only hard test failure. It can affect analyses if a downstream consumer treats `clean_skill_name` alone as the relationship grain. Current dashboard demand charts group by both skill name and type and count unique job IDs, so displayed demand values matched the implemented calculations.

2. WARNING: 26,501 jobs have no skill rows.
   This is not a calculation bug. It means total-posting KPIs/charts include postings that cannot contribute to skill charts.

3. WARNING: company-name capitalization variants exist.
   There are 2,363 normalized company-name variants. The company KPI uses `company_id`, so it is not affected. The Top Hiring Companies chart uses `clean_company_name`, so capitalization variants may split company categories.

4. WARNING: salary-range filters preserve null-salary postings.
   This is consistent with current dashboard behavior and all downstream calculations, but it may differ from a user expectation that a salary range filter only returns postings with salary values.

## Verification Commands

- `.\.venv\Scripts\python.exe -m compileall app.py views ui dashboard portfolio tests`
- `.\.venv\Scripts\python.exe -m unittest tests.test_market_dashboard_validation -v`
- Import check for dashboard modules and `views.market_dashboard`
- Full-sample audit scripts against all 150,000 hosted postings and 667,829 skill rows

Test outcome:

- 5 validation test methods ran.
- 4 passed.
- 1 failed: duplicate `(job_id, clean_skill_name)` relationship invariant.

Audit status counts from the summary table:

- PASS: 42
- FAIL: 1
- WARNING: 3
- NOT VERIFIABLE: 0

Final assessment:

- Every KPI is mathematically correct for the current dashboard definitions.
- Every chart table is mathematically correct for the current dashboard definitions.
- Filters are consistent and apply OR within filter groups and AND across filter groups.
- Production code and production data were unchanged.
