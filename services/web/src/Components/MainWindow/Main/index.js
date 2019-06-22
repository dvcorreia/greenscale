import React, { useState, useEffect } from 'react'
import { Segment, Grid } from 'semantic-ui-react'
import ListTree from './ListTree'
import Graph from './Graphs'

const Main = ({ user, ...props }) => {
    const [greenhouseData, setGreenhouseData] = useState([])
    const [telemetrics, setTelemetrics] = useState([])

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

    return (
        <Segment>
            <Grid>
                <Grid.Row columns={2} relaxed='very'>
                    <Grid.Column width={5}>
                        {greenhouseData.length === 0 ?
                            <p>No Data</p>
                            : <ListTree
                                greenhouseData={greenhouseData}
                                setTelemetrics={setTelemetrics}
                                telemetrics={telemetrics}
                            />}
                    </Grid.Column>
                    <Grid.Column width={11}>
                        {telemetrics.map((telemetric) => <Graph key={telemetric.uuid} sensor={telemetric} />)}
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </Segment>
    )
}

export default Main