import React, { useState } from 'react'
import { Form, Message, Header, Button, Select } from 'semantic-ui-react'

const NewBed = ({ data, user, setMainWindowState }) => {
    const [form, setValues] = useState({
        plant: '',
        greenhouse: ''
    })
    const [loading, setLoading] = useState(false)
    const [success, setSuccess] = useState(false)
    const [error, setError] = useState({
        value: false,
        header: '',
        content: ''
    })

    const greenhouseOptions = data.map(gh => {
        return {
            key: gh.id,
            text: gh.location + ' - ' + gh.id,
            value: gh.id
        }
    })

    const handleSelectChange = (e, { value, name }) => {
        setValues({
            ...form,
            [name]: value
        })
    }

    const updateField = e => {
        setValues({
            ...form,
            [e.target.name]: e.target.value
        })
    }

    const onSubmit = () => {
        setLoading(true)
        // Handling the user errors
        // Error for not selected greenhouse
        if (form.greenhouse.length === 0) {
            setError({
                value: true,
                header: "Greenhouse must be selected",
                content: "A greenhouse must be chosen. Please select desired greenhouse to add the sensor"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }
        // Error for empty plant
        if (form.plant.length === 0) {
            setError({
                value: true,
                header: "Plant can't be empty",
                content: "Plant can't be empty. Please fill with the specied of the bed"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }

        // Send post request
        (async () => {
            const data2send = {
                plant: form.plant
            }
            const rawResponse = await fetch('/api/v1/greenhouse/' + form.greenhouse + '/bed', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data2send)
            });
            const content = await rawResponse.json();


            if (content.status === 201) {
                setSuccess(true)
            } else {
                setError({
                    value: true,
                    header: "Error " + content.status.toString(),
                    content: content.messsage
                })
            }
        })();

        // Unset loading ...
        setLoading(false)
        setMainWindowState('main')
    }


    return (
        <Form onSubmit={onSubmit} loading={loading} error={error.value} success={success}>
            <Header as='h4'>Please, fill the form to add the new bed</Header>
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
            <Form.Field>
                <label>Plant species</label>
                <input placeholder='Strawberries ?' name='plant' value={form.plant} onChange={updateField} />
            </Form.Field>
            <Message success header='Bed added' content="Your bed was added to the database. Redirecting..." />
            <Message
                error
                header={error.header}
                content={error.content}
            />
            <Button type='submit'>Add bed</Button>
        </Form>
    )
}

export default NewBed