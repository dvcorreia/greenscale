# Greenhouse REST Service

This service provides an __API__ to the greenhouse database through __REST__ services. It handles all the information about greenhouses, their beds and sensors. 

## Operation

The operation is simple, it retrieves greenhouse data and posts greenhouse data to the greenhouse database_.
Different from the other APIs, this can retrieve information from the `uri`. This will be explicit bellow in the endpoints documentation.

## Endpoints

- [`/api/v1/greenhouse`](#`/api/v1/greenhouse`)
- [`/api/v1/greenhouse/$greenhouse/bed`](#`/api/v1/greenhouse/$greenhouse/bed`)
- [`/api/v1/greenhouse/$greenhouse/bed/$bed/sensor`](#`/api/v1/greenhouse/$greenhouse/bed/$bed/sensor`)
  
### `/api/v1/greenhouse`

This `uri` can also be written in some cases as `/api/v1/greenhouse/$greenhouse` were `$greenhouse` is the greenhouse's `id`. If you chose the first option you will have to pass the greenhouse `id` in the request body/parameters.

<p align="center"><b>GET Request</b></p>

#### Example

```bash
curl -X GET 'http://ip:port/api/v1/greenhouse?id=$id'
```

#### Parameters

- `id`: greenhouse identification

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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
     --data '{"userId":"$userId","location":"$location"}' \
     http://ip:port/api/v1/greenhouse
```

#### Body

- `userId` : identification of the user
- `location`: location of the greenhouse

#### Response

- On `201 Created`:

    ```json
    {
        "status": 201,
        "data": {
            "userId": "$userId",
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": []
            }
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

- - On `500 Internal Server Error`:

    ```json
    {
        "status": 500,
        "message": "$moreinformation"
    }
    ```

<p align="center"><b>DELETE Request</b></p>

#### Example

```bash
curl -X DELETE 'http://ip:port/api/v1/greenhouse?id=$id'
```

#### Parameters

- `id` : greenhouse identification _(this is mandatory, it cannot be passed in the request body)_

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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
curl -X PUT 'http://ip:port/api/v1/greenhouse?id=$id'
```
#### Parameters

- `id` : greenhouse identification _(this is mandatory, it cannot be passed in the request body)_

#### Body

- `location`: new location that will replace the old one

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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

 
### `/api/v1/greenhouse/$greenhouse/bed` 

This `uri` can also be written in some cases as `/api/v1/greenhouse/$greenhouse/bed/$bed` were `$greenhouse` is the greenhouse's `id` and `$bed` is the bed's `uuid`. If you chose the first option you will have to pass the bed `id` in the request body/parameters.


<p align="center"><b>POST Request</b></p>

#### Example

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"plant":"$plant"}' \
     http://ip:port/api/v1/greenhouse/$greenhouse/bed
```

#### Body

- `plant` : plant species that will be on the bed

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "bed": {
                    "uuid": "$uuid",
                    "plant": "$plant",
                    "sensors": []
                }
            }
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

- - On `500 Internal Server Error`:

    ```json
    {
        "status": 500,
        "message": "$moreinformation"
    }
    ```

<p align="center"><b>DELETE Request</b></p>

#### Example

```bash
curl -X DELETE 'http://ip:port/api/v1/greenhouse/$greenhouse/bed?uuid=$uuid'
```

#### Parameters

- `uuid` : bed identification _(this is mandatory, it cannot be passed in the request body)_

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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
curl -X PUT 'http://ip:port/api/v1/greenhouse/$greenhouse/bed?uuid=$uuid'
```
#### Parameters

- `uuid` : bed identification _(this is mandatory, it cannot be passed in the request body)_

#### Body

- `plant`: new plant species that will replace the old one

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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

- On `400 Bad request`:

    ```json
    {
        "status": 400,
        "message": "$moreinformation"
    }
    ```

 
### `/api/v1/greenhouse/$greenhouse/bed/$bed/sensor`

This `uri` can also be written in some cases as `/api/v1/greenhouse/$greenhouse/bed/$bed/sensor/$sensor` were `$greenhouse` is the greenhouse's `id`, `$bed` is the bed's `uuid` and `$sensor` is the sensor's `uuid` . If you chose the first option you will have to pass the bed `id` in the request body/parameters.


<p align="center"><b>POST Request</b></p>

#### Example

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"telemetric":"$telemetric"}' \
     http://ip:port/api/v1/greenhouse/$greenhouse/bed/$bed/sensor
```

#### Body

- `telemetric` : telemetric type that will be measured by the sensor

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": {
                    "uuid": "$uuid",
                    "sensor": {
                        "uuid": "$uuid",
                        "telemetric": "$telemetric"
                    }
                }
            }
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
    ```

- - On `500 Internal Server Error`:

    ```json
    {
        "status": 500,
        "message": "$moreinformation"
    }
    ```

<p align="center"><b>DELETE Request</b></p>

#### Example

```bash
curl -X DELETE 'http://ip:port/api/v1/greenhouse/$greenhouse/bed/$bed/sensor?uuid=$uuid'
```

#### Parameters

- `uuid` : sensor identification _(this is mandatory, it cannot be passed in the request body)_

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            }
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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
curl -X PUT 'http://ip:port/api/v1/greenhouse/$greenhouse/bed/$bed/sensor?uuid=$uuid'
```
#### Parameters

- `uuid` : sensor identification _(this is mandatory, it cannot be passed in the request body)_

#### Body

- `telemetric`: new telemetric type that will replace the old one

#### Response

- On `200 OK`:

    ```json
    {
        "status": 200,
        "data": {
            "greenhouse": {
                "id": "$id",
                "location": "$location",
                "beds": [
                    {
                        "uuid": "$bed1-uuid",
                        "plant": "$bed1-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            {
                                "uuid": "$sensor2-uuid",
                                "telemetric": "$sensor2-telemetric"
                            },
                            ...
                        ]
                    },
                    {
                        "uuid": "$bed2-uuid",
                        "plant": "$bed2-plant",
                        "sensors": [
                            {
                                "uuid": "$sensor1-uuid",
                                "telemetric": "$sensor1-telemetric"
                            },
                            ...
                        ]
                    },
                    ...
                ]
            }
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

- On `400 Bad request`:

    ```json
    {
        "status": 400,
        "message": "$moreinformation"
    }
    ```