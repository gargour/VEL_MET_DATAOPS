# 🚲⚡ Velos & Meteo DataOps Pipeline

[![DataOps CI - DBT Build & Test](https://github.com/ton-username/velos-meteo-dataops/actions/workflows/ci.yml/badge.svg)](https://github.com/ton-username/velos-meteo-dataops/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![dbt](https://img.shields.io/badge/dbt-1.12.6-orange.svg)](https://www.getdbt.com/)
[![Prefect](https://img.shields.io/badge/Prefect-v3-green.svg)](https://www.prefect.io/)
[![DuckDB](https://img.shields.io/badge/DuckDB-embedded-yellow.svg)](https://duckdb.org/)

A production-grade, end-to-end DataOps pipeline designed to ingest, transform, test, and orchestrate real-time bicycle sharing data (GBFS) and weather telemetry (Open-Meteo).

---

## 🏗️ Architecture & Tech Stack

[ Open-Meteo API & GBFS API ]
│
▼ (Ingestion)
[ dlt ] ──► [ DuckDB (Local Storage) ] ──► [ DVC (Versioning) ]
│
▼ (Transformation & Data Quality)
[ dbt ] (Staging -> Marts + Tests)
│
▼ (Orchestration)
[ Prefect 3 ]
- **Ingestion**: `dlt` (Data Load Tool) for robust schema evolution and pipeline loading.
- **Storage**: `DuckDB` as a high-performance embedded analytical data warehouse.
- **Transformation & Quality**: `dbt` (Data Build Tool) with automated unit testing (`not_null`, `unique`, `relationships`).
- **Orchestration**: `Prefect 3` for automated workflow management, retries, and monitoring.
- **Data Versioning**: `DVC` (Data Version Control) to track DuckDB state.
- **CI/CD**: `GitHub Actions` for automated integration testing on every push.

---

## 📁 Project Structure

```text
PROJET/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI workflow
├── .dvc/                      # DVC configuration
├── dbt_transform/             # dbt project directory
│   ├── models/
│   │   ├── marts/             # Dimensional models (dim_stations, fct_stations_status)
│   │   ├── staging/           # Staging views (stg_meteo, stg_stations)
│   │   └── sources.yml        # Raw sources definition
│   └── dbt_project.yml
├── orchestration/
│   └── flows.py               # Prefect end-to-end dataops flow
├── venv/                      # Python virtual environment
├── velos_meteo_pipeline.duckdb # Embedded analytical database
└── README.md