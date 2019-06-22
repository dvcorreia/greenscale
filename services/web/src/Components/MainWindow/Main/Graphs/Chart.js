import React from 'react'
import { withParentSize } from '@vx/responsive'
import { scaleTime, scaleLinear } from '@vx/scale'
import { LinePath, AreaClosed } from '@vx/shape'
import { LinearGradient } from '@vx/gradient'
import { AxisBottom, AxisLeft } from '@vx/axis'

class Chart extends React.Component {
    render() {
        const {
            parentWidth,
            parentHeight,
            data,
            telemetric
        } = this.props

        const margin = {
            top: 15,
            bottom: 40,
            left: 0,
            right: 0
        }

        const iconSensorType = (type) => {
            switch (type) {
                case 'moisture':
                    return '#0355f9'
                case 'humidity':
                    return '#0355f9'
                default:
                    return 'black'
            }
        }

        const width = parentWidth - margin.left - margin.right
        const height = parentHeight - margin.top - margin.bottom

        const x = d => new Date(d.d)
        const y = d => d.v

        const xScale = scaleTime({
            range: [0, width],
            domain: [Math.min(...data.map(x)), Math.max(...data.map(x))]
        })

        const yScale = scaleLinear({
            range: [height, 0],
            domain: [0, Math.max(...data.map(y)) + 0.25 * Math.max(...data.map(y))]
        })

        return (
            <div>
                <svg ref={s => (this.svg = s)} width={width} height={parentHeight}>
                    <LinearGradient
                        id='fill'
                        from={iconSensorType(telemetric)}
                        to='white'
                        fromOpacity={0.9}
                        toOpacity={0}
                    />
                    <AreaClosed
                        data={data}
                        x={data => xScale(x(data))}
                        y={data => yScale(y(data))}
                        yScale={yScale}
                        fill={'url(#fill)'}
                        stroke="transparent"
                    />
                    <LinePath
                        data={data}
                        x={data => xScale(x(data))}
                        y={data => yScale(y(data))}
                        stroke={iconSensorType(telemetric)}
                        strokeWidth={2}
                    />
                    <AxisBottom
                        data={data}
                        scale={xScale}
                        top={height}
                        numTicks={10}
                        stroke="black"
                        tickStroke="black"
                        tickLabelProps={() => ({
                            fill: 'black',
                            textAnchor: 'middle',
                            fontSize: 12,
                            fontFamily: 'Arial',
                        })}
                    />
                    <AxisLeft
                        data={data}
                        scale={yScale}
                        top={margin.top}
                        left={0}
                        hideZero
                        stroke="transparent"
                        tickStroke="black"
                        tickLabelProps={() => ({
                            fill: 'black',
                            textAnchor: 'middle',
                            fontSize: 12,
                            fontFamily: 'Arial',
                            dx: '1.5em'
                        })}
                    />
                </svg>
            </div>
        )
    }
}


export default withParentSize(Chart)