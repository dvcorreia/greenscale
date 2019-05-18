import React from 'react'
import { Menu, Button, Icon } from 'semantic-ui-react'

const LogStatus = ({ user }) => {
    return (
        <React.Fragment>
            <Menu.Item >
                {user.state ?
                    <React.Fragment>
                        <Button icon labelPosition='left' basic color="green">
                            <Icon name='user' color="green" />
                            {user.username}
                        </Button>
                    </React.Fragment>
                    :
                    <React.Fragment>
                        <Button icon labelPosition='left' basic color="red" disabled>
                            <Icon name='user' color="red" />
                            Log In to see your greenhouses
                        </Button>
                    </React.Fragment>
                }
            </Menu.Item>
        </React.Fragment>
    )
}

export default LogStatus