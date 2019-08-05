import React, { useState, useEffect } from 'react'
import NewGreenhouse from './NewGreenhouse'
import NewBed from './NewBed'
import NewSensor from './NewSensor'
import { Button, Container } from 'semantic-ui-react'

const New = ({ newType, setMainWindowState, user, setUser }) => {
    const [greenhouseData, setGreenhouseData] = useState([])

    useEffect(() => {
        async function fetchData() {
            const response = user.greenhouses.map(async greenhouse => {
                const response = await fetch(`/api/v1/greenhouse?id=${greenhouse}`)
                const data = await response.json()
                return data.data.greenhouse
            })

            // wait until all promises resolve
            const results = await Promise.all(response)
            return results
        }

        fetchData().then((data) => {
            setGreenhouseData(data)
        })
    }, [user.greenhouses])

    const typeManager = (newType) => {
        switch (newType) {
            case 'greenhouse':
                return <NewGreenhouse user={user} setUser={setUser} setMainWindowState={setMainWindowState} />
            case 'bed':
                return <NewBed data={greenhouseData} setMainWindowState={setMainWindowState} />
            case 'sensor':
                return <NewSensor data={greenhouseData} username={user.username} setMainWindowState={setMainWindowState} />
            default:
                return 'Loading ...'
        }
    }


    return (
        <div>
            <Container>
                <Button attached='top' onClick={() => setMainWindowState('main')}>Cancel and Back</Button>
                <br />
                {greenhouseData.length === 0 ? 'Loading ...' : typeManager(newType)}
            </Container>
        </div>
    )
}

export default New