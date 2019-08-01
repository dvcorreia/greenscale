# Discover REST Service

This service provides an __API__ to the discover database through __REST__ services. It handles the dicoverability of microcontrollers and their sensors.

## Operation

On power on, the microcontroller will send a `GET` request to the API with the `uuid` and `username` stored in the __EEPROM__. 

The API will send a request to the __search__ service questioning if the sensor bellongs to the user. 
If it does, responds `200 OK` and sends back the sensor data. The __discover__ service will route the response back to the microcontroller.

If the response from the __search__ service is `404 Not found`, the service will check if the sensor was alredy enrolled in the _discover database_.
If it was, responds back `200 OK` and the sensor information with the `username` field with empty string. This lets the microcontroller know that it doesn't bellow to a user yet.

If the sensor is not in the _discover database_, it is sent a `404 Not found`. This informs the microcontroller that it need to enroll in the __discover__ service.

To enroll in the __discover__ service, the microcontroller has to send a `POST` request to the service containing the telemetric that it will measure. The service will respond back the sensor indentification information.

The deletion of sensors enrolled in the service is taking care by the `greenhouse` service when a sensor is added to a user. It will send a `DELETE` request to the service and it will remove it from the _discover database_.

## Endpoints

### `/discover`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/discover?uuid=$uuid&username=$username'
```

#### Parameters

- `uuid` : sensor identification
- `username`: username of the user that has the sensor enrolled (multiple users can have the same sensor, this will be fixed in version `0.1.0`)  

#### Response

- On `200 OK`:

    ```json
    {
        "uuid": "$uuid",
        "telemetric": "$telemetric",
        "user": "username" || ""
    }
    ```

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$moreinformation"
    }
    ```


<p align="center"><b>POST Request</b></p>

#### Example

```bash
curl -X POST -d "" 'http://ip:port/discover?telemetric=$telemetric'
```

#### Parameters

- `telemetric` : telemetric that will me measured 

#### Response

- On `200 OK`:

    ```json
    {
        "uuid": "$uuid",
        "telemetric": "$telemetric",
        "user": ""
    }
    ```

- On `400 Bad request`:

    ```json
    {
        "status": 400,
        "message": "$moreinformation"
    }
    ```


<p align="center"><b>DELETE Request</b></p>

#### Example

```bash
curl -X DELETE 'http://ip:port/discover?uuid=$uuid'
```

#### Parameters

- `uuid` : sensor identification

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "message": "Sensor removed"
    }
    ```

- On `500 Internal Server Error` (probabily coudn't delete the sensor from the _discovery database__ for some reason):

    ```json
    {
        "status": 500,
        "message": "$moreinformation"
    }
    ```

- On `400 Bad request`:

    ```json
    {
        "status": 400,
        "message": "$moreinformation"
    }
    ```