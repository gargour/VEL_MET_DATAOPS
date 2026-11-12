{{
    config(
        materialized='incremental',
        unique_key=['station_id', 'fetched_at']
    )
}}

select
    station_id,
    num_bikes_available,
    num_docks_available,
    is_installed,
    is_renting,
    is_returning,
    fetched_at
from {{ ref('stg_stations') }}

{% if is_incremental() %}
    -- Cette condition s'exécute uniquement lors des exécutions incrémentielles (hors premier chargement complet)
    where fetched_at > (select max(fetched_at) from {{ this }})
{% endif %}