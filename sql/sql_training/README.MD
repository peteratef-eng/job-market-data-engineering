لو عايز تعمل Data Quality Check
```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(job_id) AS jobs_with_id,
    COUNT(*) - COUNT(salary_year_avg) AS missing_salary_count
FROM
    job_postings_fact;
```
Duplicate Checks
```sql
SELECT
    job_id,
    COUNT(*) AS duplicate_count
FROM
    job_postings_fact
GROUP BY
    job_id
HAVING
    COUNT(*) > 1;
```