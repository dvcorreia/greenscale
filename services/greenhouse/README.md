# Greenhouse Service

This service provides an API to the greenhouse database throught RESTfull

## Endpoints

`api/v1/greenhouse/`

    - `GET`: view greenhouse info
        Parameters:
            + id: greenhouse UUID
    - `POST`: create new greenhouse
        Body: {
            "username": username <string>,
            "location": location <string>
        }

`api/v1/greenhouse/<id>/`

    - `GET`: view greenhouse info
    - `POST`: create new greenhouse
        Body: {
            "location": location <string>
            "username": username
        }

`api/v1/greenhouse/<id>/bed/`

    - `GET`: view greenhouse's beds info
    - `POST`: create new bed
        Body: {
            "plant": plant type <string>
        }

`api/v1/greenhouse/<id>/bed/<id>/sensor/`

    - `GET`: view beds's sensors info
    - `POST`: create new sensor
        Body: {
            "uuid": uuid <string>,
            "telemetric": telemetric type <string>
        }

`api/v1/greenhouse/<id>/bed/<id>/sensor/<uuid>`

    - `POST`: create new sensor
        Body: {
            "telemetric": telemetric type <string>
        }