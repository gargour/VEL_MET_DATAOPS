select
    station_id,
    num_bikes_available,
    num_docks_available,
    load_id
from {{ ref('stg_stations') }}
where station_id is not null