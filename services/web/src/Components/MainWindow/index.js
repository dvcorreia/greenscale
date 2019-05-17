import React from 'react'
import { Dropdown, Icon, Menu, Segment } from 'semantic-ui-react'
import LogStatus from './LogStatus'
import Main from './Main'
import LogLogic from './LogLogic'


const MainWindow = ({ user, handleUser, ...props }) => {
    return (
        <div>
            <Menu size='small' attached='top'>
                <Dropdown item icon='tree' simple disabled={!user.state}>
                    <Dropdown.Menu>
                        <Dropdown.Item>
                            <Icon name='dropdown' />
                            <span className='text'>New</span>

                            <Dropdown.Menu>
                                <Dropdown.Item>Greenhouse</Dropdown.Item>
                                <Dropdown.Item>Bed</Dropdown.Item>
                                <Dropdown.Item>Sensor</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>

                <Menu.Menu position='right'>
                    <LogStatus user={user} handleUser={handleUser} />
                </Menu.Menu>
            </Menu>

            <Segment attached='bottom'>
                {user.state ? <Main /> : <LogLogic handleUser={handleUser} />}
            </Segment>
        </div>
    )
}

export default MainWindow