import duckdb

# Connexion à ta base DuckDB
con = duckdb.connect('velos_meteo_pipeline.duckdb')

# Afficher toutes les tables présentes dans le schéma raw_data
tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='raw_data'").fetchall()

print("Tables trouvées dans raw_data :")
for t in tables:
    print(f"- {t[0]}")