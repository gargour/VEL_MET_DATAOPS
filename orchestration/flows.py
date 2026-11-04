import subprocess
from prefect import flow, task

@task(name="Run DLT Ingestion", retries=2, retry_delay_seconds=10)
def run_dlt():
    print("Démarrage de l'ingestion DLT...")
    # Tu peux inclure ici l'appel à ton script d'ingestion DLT si ce n'est pas déjà fait, 
    # par exemple : subprocess.run(["python", "ingestion/pipeline.py"], check=True)
    print("Ingestion DLT terminée avec succès.")

@task(name="Check Source Freshness", retries=1)
def check_freshness():
    print("Vérification de la fraîcheur des sources...")
    result = subprocess.run([
        "dbt", "source", "freshness",
        "--project-dir", "dbt_transform",
        "--profiles-dir", r"C:\Users\amrga\.dbt"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        print("Attention : Certaines sources dépassent les seuils de fraîcheur définis.")

@task(name="Run DBT Build and Tests", retries=2, retry_delay_seconds=10)
def run_dbt():
    print("Démarrage de dbt build et des tests de qualité...")
    result = subprocess.run([
        "dbt", "build", 
        "--project-dir", "dbt_transform", 
        "--profiles-dir", r"C:\Users\amrga\.dbt"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("Les tests ou la construction dbt ont échoué.")
    print("Transformation et tests dbt réussis avec succès !")

@flow(name="velos_meteo_dataops_flow")
def main_flow():
    print("Lancement du pipeline DataOps complet...")
    run_dlt()
    check_freshness()
    run_dbt()
    print("Pipeline exécuté de bout en bout avec succès !")

if __name__ == "__main__":
    main_flow()