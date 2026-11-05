# 🚲 DataOps Pipeline : Vélos & Météo (DLT + DuckDB + dbt + Docker)

Pipeline DataOps end-to-end automatisé pour l'ingestion, la transformation et le test de données en temps réel combinant les flux des stations de vélos en libre-service (GBFS) et les prévisions météorologiques (Open-Meteo).

---

## 🛠️ Stack Technique

* **Ingestion :** `dlt` (Data Load Tool) en Python
* **Stockage :** `DuckDB` (Embedded columnar database)
* **Transformation & Tests :** `dbt` (Data Build Tool) avec l'adaptateur DuckDB
* **Orchestration :** Script Python séquentiel personnalisé (`orchestration/flows.py`)
* **Conteneurisation :** `Docker` & `Docker Compose`

---

## 📂 Structure du Projet

```text
.
├── dlt_pipeline/
│   └── ingestion.py        # Script d'ingestion des sources (GBFS & Open-Meteo) via dlt
├── dbt_transform/
│   ├── models/
│   │   ├── staging/        # Vues de staging (stg_meteo, stg_stations)
│   │   └── marts/          # Modèles dimensionnels (dim_stations, fct_stations_status)
│   ├── profiles.yml        # Configuration de la connexion DuckDB pour dbt
│   └── dbt_project.yml     # Configuration du projet dbt
├── orchestration/
│   └── flows.py            # Script d'orchestration orchestrant dlt puis dbt
├── Dockerfile              # Configuration de l'environnement conteneurisé
├── docker-compose.yml      # Orchestration du conteneur Docker
├── requirements.txt        # Dépendances Python du projet
└── README.md               # Documentation du projet
⚙️ Prérequis
Assure-toi d'avoir installé sur ta machine :

Docker Desktop en cours d'exécution.

Git (pour le versioning).

🚀 Instructions d'Installation et d'Exécution
1. Cloner le dépôt et se placer dans le dossier
PowerShell
git clone <URL_DE_TON_REPO_GITHUB>
cd <NOM_DU_PROJET>
2. Lancer le pipeline complet via Docker
Le conteneur va automatiquement installer les dépendances, exécuter l'ingestion dlt, lancer les transformations dbt et exécuter tous les tests de qualité de données.

PowerShell
docker-compose up --build
3. Vérification du succès
Le pipeline est considéré comme validé lorsque le terminal affiche le résumé final de dbt avec un statut sans erreur :

Tests exécutés : 10/10 PASS

Code de sortie : 0

Plaintext
Completed successfully
Done. PASS=10 WARN=0 ERROR=0 SKIP=0
📊 Modélisation des Données (dbt)
Le projet suit les bonnes pratiques de modélisation en couches :

Raw (Brut) : Ingestion directe des données brutes par dlt dans le schéma raw_data de DuckDB.

Staging (main_staging) : Nettoyage, typage et standardisation des champs (stg_meteo, stg_stations).

Marts (main_marts) : Modélisation dimensionnelle orientée analytique :

dim_stations : Dimension des stations de vélos (ID, nom, coordonnées).

fct_stations_status : Table de faits enregistrant l'état des vélos et des docks disponibles corrélé aux données météo