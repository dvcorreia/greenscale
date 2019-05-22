import React from 'react'
import { Menu, Button, Icon } from 'semantic-ui-react'

const LogStatus = ({ user, setUser }) => {
    const logOut = () => {
        setUser({
            id: '',
            username: '',
            greenhouses: [],
            state: false
        })
    }

    return (
        <React.Fragment>
            <Menu.Item >
                {user.state ?
                    <React.Fragment>
                        <Button icon labelPosition='left' basic color="green" onClick={logOut}>
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