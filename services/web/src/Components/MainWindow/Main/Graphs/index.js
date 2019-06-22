import React, { useState, useEffect } from 'react';
import './index.css'
import Chart from './Chart'
import { Icon } from 'semantic-ui-react'

const Graph = ({ sensor, telemetrics, setTelemetrics }) => {
  const [data, setData] = useState([])

  async function fetchData() {
    const response = await fetch(`/api/v1/${sensor.telemetric}?uuid=${sensor.uuid}&size=100`)
    return response.json()
  }

  const iconSensorType = (type) => {
    switch (type) {
      case 'moisture':
        return 'tint'
      case 'humidity':
        return 'umbrella'
      default:
        return 'folder'
    }
  }

  useEffect(() => {
    fetchData().then(r => setData(r.data))
  }, [])

  return (
    <div className='graph-container'>
      <div className='chart'>
        <div className='titlebar'>
          <div className='title'>
            {sensor.uuid + ' '}
            <small>
              ({sensor.telemetric} <Icon size='small' name={iconSensorType(sensor.telemetric)} />)
            </small>
          </div>
          <div className='spacer' />
          <div className='currentValue'>
            <Icon circular link inverted color='green' size='small' name='redo'
              onClick={() => {
                fetchData().then(r => setData(r.data))
              }}
            />
            <Icon circular link inverted color='red' size='small' name='close' onClick={() => {
              console.log('pressed')
              setTelemetrics(telemetrics.filter(t => t.uuid !== sensor.uuid))
            }} />
          </div>
        </div>
        <div className='container'>
          <Chart data={data} telemetric={sensor.telemetric} />
        </div>
      </div>
    </div>
  );
}

export default Graph;
