# Telemetric REST Service

This service provides an __API__ to the `POST` and `GET` the telemetrics data. This service can be reused for every type of sensor data, so with telemetric, we mean humidity, moisture and light, e.g.

## Operation

The service, when started, looks for and environment variable called `TELEMETRIC` that specifies the type of the sensorial data that will be handling. Each instance of this service can only serve requests of the chosen telemetric.

This is how it needs to be architectured: each telemetric service needs to have it's own database that follows the standard name `db-$telemetric`, where `$telemetric` is the one specified in the environment variable `TELEMETRIC`. This provides independent scalability between telemetrics. If you want more moisture sensors than humidity sensors, you can scale the db and the services independently. In case of one service or db goes down, the other telemetrics can still be able to `POST` and `GET` data.  

## Endpoints

### `/$telemetric` 

`$telemetric` must be substituted with the one specified in the `TELEMETRIC` environment variable. Beyond this point, if we reference `$telemetric`, remember that is the telemetric specified.  

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/$telemetric?uuid=$uuid&size=$size'
```

#### Parameters

- `uuid` : sensor identification
- `size`: the number of measurements you want to retrieve. If the asked number is above the measurements in the database, it will send back all the measurements it has. _(Optional, if not specified, every measurement is sent back, so please specify it - this will be fixed in version `0.1.0`)_

> At this moment, is not possible to specify data between to dates/times. This will be added in version `0.1.0`.


#### Response

- On `200 OK`:

    ```json
    {
        "sensorId": "$uuid",
        "data": [
            {
                "v": "$value",
                "d": "$date"
            },
            {
                "v": "$value",
                "d": "$date"
            },
            {
                "v": "$value",
                "d": "$date"
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


<p align="center"><b>POST Request</b></p>

#### Example

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"sensor":"$uuid","value":"$value"}' \
    http://ip:port/$telemetric
```

#### Body

The content type is `json`.

```json
{
    "sensor": "$uuid",
    "value": "$value_measured"
}
```

#### Response

- On `200 OK`:

    ```json
    {
        "response": "Posted with the id"
    }
    ```

- On `400 Bad request`:

    ```json
    {
        "status": 400,
        "message": "$moreinformation"
    }
    ```