# Actuator REST Service

This service provides an __API__ to the actuator database through __REST__ services. It handles the retrieving of actuator information. It also enrolls new actuator through this service.

The received information will follow the following schema: 

## Endpoints

 - [`/api/v1/actuator`](#`/actuator`)

### `/actuator`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/actuator?uuid=$uuid'
```

#### Parameters

- `uuid`: the identification of the actuator

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "oid": "$actuator_objectId",
            "uuid": "$actuator_id",
            "description": "$description",
            "time": "$time_to_on",
            "ip": "$ip_if_there_is_one"
        }
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
     --data '{"description":"$description","time":"$time","ip":"$ip"}' \
     http://ip:port/api/v1/actuator
```

#### Body

- `description`: description of the warning 
- `time`: if momentary actuation, defines the time of that actuation
- `ip`: ip of the actuator _(optional)_

#### Response

- On `201 Created`:

    ```json
    {
        "status": 201,
        "data": {
            "oid": "$actuator_objectId",
            "uuid": "$actuator_id",
            "description": "$description",
            "time": "$time_to_on",
            "ip": "$ip_if_there_is_one"
        }
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
curl -X DELETE 'http://ip:port/api/v1/actuator?uuid=$uuid'
```

#### Parameters

- `uuid` :  the identification of the actuator

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "description": "Actuator deleted"
    }
    ```

- On `500 Internal Server Error`:

    ```json
    {
        "status": 500,
        "message": "$moreinformation"
    }
    ```

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$moreinformation"
    }
    ```