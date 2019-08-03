# Search REST Service

This service provides an __API__ to search for sensors, beds and greenhouses. The service communicates with the __greenhouse__ service and to gather the data and parse it, providing it's services through a __REST__ API.

## Operation

> At this point, the API only provides the search of __sensors__ providing a `username` and `uuid`. This will be fixed in version `0.1.0`.

The service receives the request and sends a request to the __greenhouse__ service, that gives the data asked back. The data is then searched and returned. There is no access to the main database in this service. Depending on changes in the architecture, in the future it might have.

## Endpoints

### `/api/v1/search`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/search?uuid=$uuid&username=$username'
```

#### Parameters

- `uuid` : sensor identification
- `username`: username of the user that has the sensor enrolled

#### Response

- On success `200 OK`:

    ```json
    {
        "status": 200,
        "sensor": {
            "uuid": "$uuid",
            "telemetric": "$telemetric"
        }
    }
    ```

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$message"
    }
    ```

- On `500 Internal Server Error`:
  
    ```json
    {
        "status": 505,
        "message": "$message"
    }
    ```