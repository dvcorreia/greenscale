import React from 'react'
import { List } from 'semantic-ui-react'
import GreehouseTree from './GreenhouseTree'

const ListTree = ({ greenhouseData, ...props }) => {
    return (
        <List>
            {greenhouseData.map((greenhouse) => {
                return <GreehouseTree
                    key={greenhouse.id}
                    greenhouse={greenhouse}
                    {...props}
                />
            })}
        </List>
    )
}

export default ListTree