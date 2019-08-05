import React, { useState, useEffect } from 'react'
import { Form, Message, Header, Button, Select } from 'semantic-ui-react'

const NewSensor = ({ data, username, setMainWindowState }) => {
    const [form, setValues] = useState({
        greenhouse: '',
        bed: '',
        sensor: '',
        sensorTelemetric: ''
    })
    const [loading, setLoading] = useState(false)
    const [success, setSuccess] = useState(false)
    const [error, setError] = useState({
        value: false,
        header: '',
        content: ''
    })
    const [sensorOptions, setSensorOptions] = useState([])

    useEffect(() => {
        (async () => {
            const rawResponse = await fetch('/api/v1/discover/all?username=' + username)
            const content = await rawResponse.json();

            const sensor_parsed = content.sensors.map(s => {
                return {
                    key: s.uuid,
                    text: s.telemetric + ' - ' + s.uuid,
                    value: s.uuid
                }
            })

            setSensorOptions(sensor_parsed)
        })();
    }, [setSensorOptions])

    const handleSensorChange = (e, { value, name }) => {
        const sensor = sensorOptions.find(s => {
            return s.key === value
        })
        const telemetric_s = sensor.text.split(" ")
        setValues({
            ...form,
            [name]: value,
            sensorTelemetric: telemetric_s[0]
        })
    }


    const handleSelectChange = (e, { value, name }) => {
        setValues({
            ...form,
            [name]: value
        })
    }

    const onSubmit = () => {
        // Set loading ...
        setLoading(true)

        // Handling the user errors
        // Error from not selected greenhouse
        if (form.greenhouse.length === 0) {
            setError({
                value: true,
                header: "Greenhouse must be selected",
                content: "Greenhouse must be selected. Please select one of the greenhouses"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }

        // Error from not selected bed
        if (form.bed.length === 0) {
            setError({
                value: true,
                header: "Bed must be selected",
                content: "Bed must be selected. Please select one of the beds"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }

        // Error from not selected sensor
        if (form.sensor.length === 0) {
            setError({
                value: true,
                header: "Sensor must be selected",
                content: "Sensor must be selected. Please select one of the sensors"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }

        // Send post request
        (async () => {
            const data2send = {
                telemetric: form.sensorTelemetric,
                uuid: form.sensor
            }
            const rawResponse = await fetch('/api/v1/greenhouse/' + form.greenhouse + '/bed/' + form.bed + '/sensor', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data2send)
            });
            const content = await rawResponse.json();

            if (content.status === 200) {
                setSuccess(true)
            } else {
                setError({
                    value: true,
                    header: "Error " + content.status.toString(),
                    content: content.message
                })
                return setLoading(false)
            }
        })();

        // Unset loading ...
        setLoading(false)
        setMainWindowState('main')
    }

    const greenhouseOptions = data.map(gh => {
        return {
            key: gh.id,
            text: gh.location + ' - ' + gh.id,
            value: gh.id
        }
    })

    const genbedOptions = () => {
        if (form.greenhouse.length === 0) return []

        const gh2find = data.find(gh => {
            return gh.id === form.greenhouse
        })

        const beds = gh2find.beds.map(b => {
            return {
                key: b.uuid,
                text: b.plant + ' - ' + b.uuid,
                value: b.uuid
            }
        })

        return beds
    }

    const bedOptions = genbedOptions()

    return (
        <Form onSubmit={onSubmit} loading={loading} error={error.value} success={success}>
            <Header as='h3'>Please, fill the form to add the new sensor</Header>
            <Header as='h4'>Chose the greenhouse to add the new sensor</Header>
            <Form.Field
                control={Select}
                options={greenhouseOptions}
                label={{ children: 'Greenhouse', htmlFor: 'form-select-control-greenhouse' }}
                placeholder='Greenhouse'
                search
                searchInput={{ id: 'form-select-control-greenhouse' }}
                name='greenhouse'
                onChange={handleSelectChange}
            />
            <Header as='h4'>Chose the bed to add the new sensor</Header>
            <Form.Field
                disabled={form.greenhouse.length === 0 ? true : false}
                control={Select}
                options={bedOptions}
                label={{ children: 'Bed', htmlFor: 'form-select-control-bed' }}
                placeholder='Greenhouse'
                search
                searchInput={{ id: 'form-select-control-bed' }}
                name='bed'
                onChange={handleSelectChange}
            />
            <Header as='h4'>Chose the sensor to add (those are the ones available)</Header>
            <Form.Field
                control={Select}
                options={sensorOptions}
                label={{ children: 'Sensor', htmlFor: 'form-select-control-sensor' }}
                placeholder='Sensor'
                search
                searchInput={{ id: 'form-select-control-sensor' }}
                name='sensor'
                onChange={handleSensorChange}
            />
            <Message success header='Sensor added' content="Your sensor was added to the database. Redirecting..." />
            <Message
                error
                header={error.header}
                content={error.content}
            />
            <Button type='submit'>Add sensor</Button>
        </Form>
    )
}

export default NewSensor