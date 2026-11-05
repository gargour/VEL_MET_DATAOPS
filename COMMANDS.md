🚲⚡ Velos & Meteo DataOps - Executive Cheat Sheet

This document centralizes all commands required to run, test, document, and manage the end-to-end DataOps pipeline on Windows.

1. Environment Setup & Activation

Activate the virtual environment in PowerShell:

.\venv\Scripts\Activate.ps1


2. Full Pipeline Orchestration (Prefect 3 & dlt)

Execute the complete end-to-end ELT pipeline (Ingestion -> Freshness Checks -> dbt Transformations -> Data Quality Unit Tests):

python orchestration/flows.py


3. Data Transformation & Quality Testing (dbt)

Navigate to the dbt project root:

cd dbt_transform


Build & Test

Run all SQL views, dimensional models, and primary/foreign key data contract tests (not_null, unique, relationships):

dbt build


Documentation & Lineage Graph

Generate catalog artifacts:

dbt docs generate


Serve the interactive lineage graph UI (using port 8085 to avoid conflicts with local Jenkins on 8080):

dbt docs serve --port 8085


4. Version Control & CI/CD Operations (Git & GitHub)

Clean local unreachable objects (housekeeping):

git gc --prune=now


Inspect working tree status:

git status


Commit and trigger automated GitHub Actions CI/CD pipeline (ci.yml):

git add .
git commit -m "feat: updates to dataops pipeline and documentation"
git push origin main


5. Summary Architecture Quick Reference

Ingestion: dlt (Data Load Tool)

Analytical Storage: DuckDB (velos_meteo_pipeline.duckdb)

Transformation & Data Quality: dbt (dbt_transform/)

Orchestration: Prefect 3 (orchestration/flows.py)

Data Versioning: DVC

Automation: GitHub Actions (.github/workflows/ci.yml)