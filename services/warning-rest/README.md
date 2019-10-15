# Warning REST Service

This service provides an __API__ to the warning database through __REST__ services. It handles the retrieving of warning data. Can also POST warnings through this service.

The received information will follow the following schema: 

```json
{
    "target": "$target_uuid",
    "description": "$description"
}
```

And will be saved as:

```json
{
    "target": "$target_uuid",
    "description": "$description",
    "date": "$data.now"
}
```

## Endpoints

 - [`/api/v1/warning`](#`/warning`)

### `/warning`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/warning?uuid=$target_uuid'
```

#### Parameters

- `uuid`: the identification of the target of warning

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": [
            {
                "oid": "warning_object_id",
                "target": "$target_uuid",
                "description": "$description",
                "date": "$data.now"
            },{
                "oid": "warning_object_id",
                "target": "$target_uuid",
                "description": "$description",
                "date": "$data.now"
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
     --data '{"target":"$target_uuid","description":"$description"}' \
     http://ip:port/api/v1/warning
```

#### Body

- `target` : the identification of the target of warning
- `description`: description of the warning 

#### Response

- On `201 Created`:

    ```json
    {
        "status": 201,
        "data": {
            "oid": "warning_object_id",
            "target": "$target_uuid",
            "description": "$description",
            "date": "$data.now"
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

__Deletes all warnings on target.__

```bash
curl -X DELETE 'http://ip:port/api/v1/warning?uuid=$target_uuid'
```

#### Parameters

- `uuid` :  the identification of the target of warning

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "description": "Warnings deleted"
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