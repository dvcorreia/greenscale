import React, { useState } from 'react'
import { Form, Button, Header, Message } from 'semantic-ui-react'

const NewGreenhouse = ({ user, setUser, setMainWindowState }) => {
    const [form, setValues] = useState({
        location: ''
    })
    const [loading, setLoading] = useState(false)
    const [success, setSuccess] = useState(false)
    const [error, setError] = useState({
        value: false,
        header: '',
        content: ''
    })

    const updateField = e => {
        setValues({
            ...form,
            [e.target.name]: e.target.value
        })
    }

    const onSubmit = () => {
        // Set loading ...
        setLoading(true)

        // Handling the user errors
        if (form.location.length === 0) {
            setError({
                value: true,
                header: "Location can't be empty",
                content: "Location can't be empty. Please fill with the location of the greenhouse"
            })
            return setLoading(false)
        } else {
            if (error.value) setError(false)
        }

        // Send post request
        (async () => {
            const data2send = {
                userId: user.id,
                location: form.location
            }
            const rawResponse = await fetch('/api/v1/greenhouse', {
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
                setUser({
                    ...user,
                    greenhouses: [...user.greenhouses, content.data.greenhouse.id]
                })
            } else {
                setError({
                    value: true,
                    header: "Error " + content.status.toString(),
                    content: content.message
                })
            }
        })();

        // Unset loading ...
        setLoading(false)
        setMainWindowState('main')
    }

    return (
        <Form onSubmit={onSubmit} loading={loading} error={error.value} success={success}>
            <Header as='h4'>Please, fill the form to add the new greenhouse</Header>
            <Form.Field>
                <label>Location</label>
                <input placeholder='Milan ?' name='location' value={form.location} onChange={updateField} />
            </Form.Field>
            <Message success header='Greenhouse added' content="Your greenhouse was added to the database. Redirecting..." />
            <Message
                error
                header={error.header}
                content={error.content}
            />
            <Button type='submit'>Add greenhouse</Button>
        </Form>
    )
}

export default NewGreenhouse