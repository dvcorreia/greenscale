# Humidity Service

This service provides an API to the humidity database throught RESTfull and MQTT services

## Endpoints

`api/v1/humidity/`

    - `GET`: view sensor data
        Parameters:
            + sensorId: sensor UUID
            + start: start data point
            + n: number of data points
    - `POST`: create new telemetric for sensors
        Body: {
            "sensorId": UUID
            "value": DecimalString
            "date": Date (optional)
        }

`api/v1/humidity/<uuid>/`

    - `GET`: view sensor data
        Parameters:
            + start: start data point
            + n: number of data points
    - `POST`: create new telemetric for sensors
        Body: {
            "value": DecimalString
            "date": Date (optional)
        }
