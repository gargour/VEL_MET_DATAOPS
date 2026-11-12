{{
    config(
        materialized='table'
    )
}}

select distinct
    station_id
from {{ ref('stg_stations') }}
where station_id is not null