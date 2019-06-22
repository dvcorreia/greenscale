import React, { useState, useEffect } from 'react';
import './index.css'
import Chart from './Chart'

const Background = ({ width, height }) => {
  return (
    <svg width={width} height={height}>
      <rect width={width} height={height} fill='white' />
    </svg>
  )
}

const Graph = ({ sensor }) => {
  const [data, setData] = useState([])

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`/api/v1/${sensor.telemetric}?uuid=${sensor.uuid}&size=100`)
      return response.json()
    }

    fetchData().then(r => setData(r.data))
  }, [])

  const currentValue = data.length === 0 ? '' : data[data.length - 1].v
  console.log(data)

  return (
    <div className='graph-container'>
      <div className='chart'>
        <div className='titlebar'>
          <div className='title'>
            {sensor.uuid}
          </div>
          <div className='spacer' />
          <div className='currentValue'>
            cv: {currentValue}
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
