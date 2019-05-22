import React from 'react'
import { List } from 'semantic-ui-react'
import SensorTree from './SensorTree'

const BedTree = ({ bed, ...props }) => {
    const [selected, setSelected] = React.useState(false)

    return (
        <List.Item>
            <List.Icon
                name='leaf'
                color={selected ? 'green' : 'black'}
                onClick={() => setSelected(!selected)}
            />
            <List.Content>
                <List.Header>{bed.plant}</List.Header>
                <List.Description>{bed.uuid}</List.Description>
                {selected ? <List.List>
                    {bed.sensors.map((sensor) => {
                        return <SensorTree
                            key={sensor.uuid}
                            sensor={sensor}
                            {...props}
                        />
                    })}
                </List.List> : ''}
            </List.Content>
        </List.Item>
    )
}

export default BedTree