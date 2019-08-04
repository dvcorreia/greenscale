import React, { useState } from 'react'
import { Dropdown, Icon, Menu, Segment } from 'semantic-ui-react'
import LogStatus from './LogStatus'
import Main from './Main'
import LogLogic from './LogLogic'
import New from './New'


const MainWindow = ({ user, setUser, ...props }) => {
    const [mainWindowState, setMainWindowState] = useState(['main'])

    const mainWindowManager = (windowState) => {
        if (windowState == 'main') {
            return <Main user={user} />
        } else {
            return <New newType={windowState} setMainWindowState={setMainWindowState} user={user} setUser={setUser} />
        }
    }

    return (
        <div>
            <Menu size='small' attached='top'>
                <Dropdown item icon='tree' simple disabled={!user.state}>
                    <Dropdown.Menu>
                        <Dropdown.Item>
                            <Icon name='dropdown' />
                            <span className='text'>New</span>
                            <Dropdown.Menu>
                                <Dropdown.Item onClick={() => setMainWindowState('greenhouse')}>Greenhouse</Dropdown.Item>
                                <Dropdown.Item onClick={() => setMainWindowState('bed')}>Bed</Dropdown.Item>
                                <Dropdown.Item onClick={() => setMainWindowState('sensor')}>Sensor</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>

                <Menu.Menu position='right'>
                    <LogStatus user={user} setUser={setUser} />
                </Menu.Menu>
            </Menu>

            <Segment attached='bottom'>
                {user.state ? mainWindowManager(mainWindowState) : <LogLogic setUser={setUser} />}
            </Segment>
        </div>
    )
}

export default MainWindow