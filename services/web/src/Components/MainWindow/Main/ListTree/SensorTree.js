import React, { useState } from 'react'
import { List } from 'semantic-ui-react'

const SensorTree = ({ sensor, setTelemetrics, telemetrics }) => {
    const [selected, setSelected] = useState(telemetrics.filter(s => s.uuid === sensor.uuid).length !== 0 ? true : false)

    const handleOnClick = () => {
        selected ?
            setTelemetrics(telemetrics.filter(s => s.uuid !== sensor.uuid))
            :
            setTelemetrics([...telemetrics, sensor])

        setSelected(!selected)
    }

    const iconSensorType = (type) => {
        switch (type) {
            case 'moisture':
                return 'tint'
            case 'humidity':
                return 'umbrella'
            default:
                return 'folder'
        }
    }

    return (
        <List.Item>
            <List.Icon
                name={iconSensorType(sensor.telemetric)}
                color={selected ? 'orange' : 'black'}
                onClick={handleOnClick}
            />
            <List.Content>
                <List.Header>{sensor.telemetric}</List.Header>
                <List.Description>{sensor.uuid}</List.Description>
            </List.Content>
        </List.Item>
    )
}

export default SensorTree