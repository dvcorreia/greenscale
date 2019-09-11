# Discover REST Service

This service provides an __API__ to the discover database through __REST__ services. It handles the discoverability of microcontrollers and their sensors.

## Operation

On power on, the microcontroller will send a `GET` request to the API with the `uuid` and `username` stored in the __EEPROM__. 

The API will send a request to the __search__ service questioning if the sensor belongs to the user. 
If it does, responds `200 OK` and sends back the sensor data. The __discover__ service will route the response back to the microcontroller.

If the response from the __search__ service is `404 Not found`, the service will check if the sensor was already enrolled in the _discover database_.
If it was, responds back `200 OK` and the sensor information with the `username` field with empty string. This lets the microcontroller know that it doesn't bellow to a user yet.

If the sensor is not in the _discover database_, it is sent a `404 Not found`. This informs the microcontroller that it need to enroll in the __discover__ service.

To enroll in the __discover__ service, the microcontroller has to send a `POST` request to the service containing the telemetric that it will measure and the username. The service will respond back the sensor identification information.

The deletion of sensors enrolled in the service is taking care by the `greenhouse` service when a sensor is added to a user. It will send a `DELETE` request to the service and it will remove it from the _discover database_.

In case the `uuid` was generated at the time of the microcontroller software flash you can hit the API on the _/api/v1/discover/enroll_ sending the `username`, `uuid` and `telemetric` as parameters. This will let the service know and update on the state of the sensor. This request can be sent every time the microcontroller is turned on.

## Endpoints

- [`/api/v1/discover`](#`/api/v1/discover`)
- [`/api/v1/discover/all`](#`/api/v1/discover/all`)
- [`/api/v1/discover/enroll`](#`/api/v1/discover/enroll`)

### `/api/v1/discover`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/discover?uuid=$uuid&username=$username'
```

#### Parameters

- `uuid`: uuid of the sensor
- `username`: username of the user that has the sensor enrolled

#### Response

- On `200 OK`:

    ```json
    {
        "uuid": "$uuid",
        "telemetric": "$telemetric",
        "user": "" || "$username"
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
curl -X POST -d "" 'http://ip:port/api/v1/discover?telemetric=$telemetric&username=$username'
```

#### Parameters

- `telemetric` : telemetric that will me measured 
- `username`: username of the user

#### Response

- On `200 OK`:

    ```json
    {
        "uuid": "$uuid",
        "telemetric": "$telemetric",
        "user": "$username"
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
curl -X DELETE 'http://ip:port/api/v1/discover?uuid=$uuid'
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

- On `500 Internal Server Error` (probably couldn't delete the sensor from the _discovery database__ for some reason):

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


### `/api/v1/discover/all`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/discover/all?username=$username'
```

#### Parameters

- `username`: username of the user that has the sensor enrolled

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "sensors": [
        {
            "uuid": "$uuid1",
            "telemetric": "$telemetric1"
        },
        {
            "uuid": "$uuid2",
            "telemetric": "$telemetric2"
        },
        ...
        ]
    }
    ```

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$moreinformation"
    }
    ```


### `/api/v1/discover/enroll`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/discover/enroll?uuid=$uuid&username=$username&telemetric=$telemetric'
```

#### Parameters

- `uuid`: uuid of the sensor
- `username`: username of the user that has the sensor enrolled
- `telemetric`: telemetric type of the sensor

#### Response

- On `200 OK`:

    ```json
    {
        "uuid": "$uuid",
        "telemetric": "$telemetric",
        "user": "" || "$username"
    }
    ```

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$moreinformation"
    }
    ```