import os
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

# Extract CSV Files
companies_df = pd.read_csv("data/company_dim.csv")
jobs_df = pd.read_csv("data/job_postings_fact.csv")
skills_df = pd.read_csv("data/skills_dim.csv")
skills_jobs_df = pd.read_csv("data/skills_job_dim.csv")

print("CSV Files loaded into pandas")

print("companies:", companies_df.shape)
print("jobs:", jobs_df.shape)
print("skills:", skills_df.shape)
print("skills_jobs:", skills_jobs_df.shape)

# Load into PostgreSQL
companies_df.to_sql(
    "company_dim",
    engine,
    if_exists="replace",
    index=False
)

jobs_df.to_sql(
    "job_postings_fact",
    engine,
    if_exists="replace",
    index=False
)

skills_df.to_sql(
    "skills_dim",
    engine,
    if_exists="replace",
    index=False
)

skills_jobs_df.to_sql(
    "skills_job_dim",
    engine,
    if_exists="replace",
    index=False
)

print("Project data loaded successfully into PostgreSQL")