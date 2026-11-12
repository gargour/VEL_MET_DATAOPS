{{
    config(
        materialized='table'
    )
}}

select
    time as observation_time,
    temperature_2m as temperature,
    weather_code,
    interval
from {{ ref('stg_meteo') }}
where time is not null