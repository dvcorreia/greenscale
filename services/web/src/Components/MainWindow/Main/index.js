import React, { useState, useEffect } from 'react'
import { Segment, Grid, Divider } from 'semantic-ui-react'
import ListTree from './ListTree'

const Main = ({ user, ...props }) => {
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
            console.log(data)
        })
    }, [])

    return (
        <Segment>
            <Grid>
                <Grid.Row columns={2} relaxed='very'>
                    <Grid.Column>
                        {greenhouseData.length === 0 ? <p>No Data</p> : <ListTree />}
                    </Grid.Column>
                    <Grid.Column>
                        <h2>Data Visualization</h2>
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </Segment>
    )
}

export default Main