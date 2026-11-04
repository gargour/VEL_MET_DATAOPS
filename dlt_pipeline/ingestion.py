import dlt
import requests

@dlt.resource(name="stations_gbfs", write_disposition="append")
def get_gbfs_stations():
    # Endpoint GBFS public ultra-stable (Capital Bikeshare / System Status)
    url = "https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    stations = data.get("data", {}).get("stations", [])
    for station in stations:
        yield station

@dlt.resource(name="meteo_open_meteo", write_disposition="append")
def get_open_meteo():
    # Open-Meteo pour Washington DC (coordonnées correspondantes au réseau de vélos)
    url = "https://api.open-meteo.com/v1/forecast?latitude=38.8951&longitude=-77.0364&current=temperature_2m,precipitation,weather_code"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    current_weather = data.get("current", {})
    yield current_weather

@dlt.source
def velos_meteo_source():
    return [get_gbfs_stations(), get_open_meteo()]

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="velos_meteo_pipeline",
        destination="duckdb",
        dataset_name="raw_data"
    )
    
    load_info = pipeline.run(velos_meteo_source())
    print(load_info)