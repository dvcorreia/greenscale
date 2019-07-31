# User Service

This service provides an API to the user database throught RESTfull

## Endpoints

`api/v1/user/`

    - `GET`: get user data
        Parameters:
            + username: username string
    - `POST`: create new user
        Body: {
            "username": username string
        }

`api/v1/user/<username>`

    - `GET`: get user data
    - `POST`: create new user

`api/v1/user/<username>/greenhouse/`

    - `GET`: get user greenhouses data
    - `POST`: create new greenhouse