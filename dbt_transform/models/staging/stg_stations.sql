select
    station_id,
    num_bikes_available,
    num_docks_available,
    is_installed,
    is_renting,
    is_returning,
    last_reported as fetched_at
from {{ source('raw_data', 'stations_gbfs') }}