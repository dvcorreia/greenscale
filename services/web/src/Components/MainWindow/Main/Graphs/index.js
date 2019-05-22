import React, { useEffect, useState } from 'react'

const Graph = ({ sensor }) => {
    const [data, setData] = useState([])

    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`/api/v1/${sensor.telemetric}?uuid=${sensor.uuid}&size=3`)
            return response.json()
        }

        fetchData().then(r => console.log(r))
    })

    return (
        <h5>{sensor.uuid}</h5>
    )
}

export default Graph