select distinct
    station_id,
    is_installed,
    is_renting,
    is_returning
from {{ ref('stg_stations') }}
where station_id is not null