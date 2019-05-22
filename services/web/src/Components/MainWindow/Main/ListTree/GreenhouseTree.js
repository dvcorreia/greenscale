import React from 'react'
import { List } from 'semantic-ui-react'
import BedTree from './BedTree'

const GreenhouseTree = ({ greenhouse, ...props }) => {
    const [selected, setSelected] = React.useState(false)

    return (
        <List.Item>
            <List.Icon
                name='warehouse'
                color={selected ? 'green' : 'black'}
                onClick={() => setSelected(!selected)}
            />
            <List.Content>
                <List.Header>{greenhouse.location}</List.Header>
                <List.Description>{greenhouse.id}</List.Description>
                {selected ? <List.List>
                    {greenhouse.beds.map((bed) => {
                        return <BedTree
                            key={bed.uuid}
                            bed={bed}
                            {...props}
                        />
                    })}
                </List.List> : ''}
            </List.Content>
        </List.Item>
    )
}

export default GreenhouseTree