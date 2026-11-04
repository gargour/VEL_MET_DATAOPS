select
    station_id,
    num_bikes_available,
    num_docks_available,
    is_installed,
    is_renting,
    is_returning,
    _dlt_load_id as load_id,
    _dlt_id as record_id
from {{ source('raw_data', 'stations_gbfs') }}