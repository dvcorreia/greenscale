import React, { useState, useEffect } from 'react';
import './index.css'
import Chart from './Chart'
import { Icon } from 'semantic-ui-react'

const Graph = ({ sensor, telemetrics, setTelemetrics }) => {
  const [data, setData] = useState([])

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`/api/v1/${sensor.telemetric}?uuid=${sensor.uuid}&size=100`)
      return response.json()
    }

    fetchData().then(r => setData(r.data))
  }, [])

  return (
    <div className='graph-container'>
      <div className='chart'>
        <div className='titlebar'>
          <div className='title'>
            {sensor.uuid}
            <small>({sensor.telemetric})</small>
          </div>
          <div className='spacer' />
          <div className='currentValue'>
            <Icon circular link inverted color='green' size='small' name='redo' />
            <Icon circular link inverted color='red' size='small' name='close' onClick={() => {
              console.log('pressed')
              setTelemetrics(telemetrics.filter(t => {
                console.log(t)
                return t.uuid !== sensor.uuid
              }))
            }} />
          </div>
        </div>
        <div className='container'>
          <Chart data={data} />
        </div>
      </div>
    </div>
  );
}

export default Graph;
