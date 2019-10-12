# User REST Service

This service provides an __API__ to the users database through __REST__ services. It handles the sign in and log in of users. It also registers which greenhouses the user has access to.

## Operation

The operation is fairly simple: it retrieves user data and posts user data to the _user database_. In the database is saved the `username`, `id` and an access list of `greenhouses`  for each user.

## Endpoints

 - [`/api/v1/user`](#`/user`)
 - [`/api/v1/user/greenhouse`](#`/user/greenhouse`)

### `/user`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/user?username=$username'
```

#### Parameters

- `username`: username of the user 

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "id": "$id",
            "username": "$username",
            "greenhouses": [ 
                "$idgh1", 
                "$idgh2", 
                "idgh3", 
                ...
            ]
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
     --data '{"username":"$username"}' \
     http://ip:port/api/v1/user
```

#### Body

- `username` : username of the user 

#### Response

- On `201 Created`:

    ```json
    {
        "status": 201,
        "data": {
            "id": "$id",
            "username": "$username",
            "greenhouses": []
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
curl -X DELETE 'http://ip:port/api/v1/user?id=$id'
```

#### Parameters

- `id` : user identification

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "description": "User deleted",
        "user": {
            "id": "$id",
            "username": "$username"
        }
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


<p align="center"><b>PUT Request</b></p>

#### Example

```bash
curl -X PUT 'http://ip:port/api/v1/user?id=$id'
```

#### Body

- `id` : user identification
- `username` : username that you will change too _(optional)_

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "description": "User deleted",
        "user": {
            "id": "$id",
            "username": "$username",
            "greenhouses": [ 
                "$idgh1", 
                "$idgh2", 
                "idgh3", 
                ...
            ]
        }
    }
    ```

- On `400 Bad Request` :

    ```json
    {
        "status": 400,
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

### `/user/greenhouse`

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/user/greenhouse?username=$username'
```

#### Parameters

- `username`: username of the user 

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouses": [ 
                "$idgh1", 
                "$idgh2", 
                "idgh3", 
                ...
            ]
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
     --data '{"greenhouses":[$greenhouses]}' \
     'http://ip:port/api/v1/user/greenhouse?userId=$userId'
```

#### Parameters

- `userId` : id of the user 

#### Body

- `[greenhouses]` : list of greenhouses id _(in this version there is only the greenhouses to update)_ 

#### Response

- On `201 Created`:

    ```json
    {
        "status": 201,
        "data": {
            "id": "$id",
            "username": "$username",
            "greenhouses": [ 
                "$idgh1", 
                "$idgh2", 
                "idgh3", 
                ...
            ]
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

- On `404 Not found`:

    ```json
    {
        "status": 404,
        "message": "$moreinformation"
    }

- On `204 No Content`:

    ```json
    {
        "status": 204,
        "message": "$moreinformation"
    }
    ```


<p align="center"><b>DELETE Request</b></p>

#### Example

```bash
curl -X DELETE 'http://ip:port/api/v1/user/greenhouse?userId=$userId&greenhouseId=$greenhouseId'
```

#### Parameters

- `userId` : user identification
- `greenhouseId`: greenhouse identification to remove from user

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "description": "Greenhouse removed from User's greenhouses",
        "user": {
            "id": "$id",
            "username": "$username",
            "greenhouses": [ 
                "$idgh2", 
                "idgh3", 
                ...
            ]
        }
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
