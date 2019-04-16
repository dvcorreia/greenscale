# Moisture Service

This service provides an API to the moisture database throught RESTfull and MQTT services

## Endpoints

`api/v1/<user-id>/greenhouse/<id>/moisture/`

    - `GET`: view sensors collection
    - `POST`: create new telemetric for sensors

`api/v1/<user-id>/greenhouse/<id>/moisture/<id>/`

    - `GET`: view sensor collection
    - `POST`: create new telemetric

