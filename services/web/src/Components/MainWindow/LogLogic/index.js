import React, { useState } from 'react'
import { Form, Button, FormField, Container, Message, Icon } from 'semantic-ui-react'


const LogLogic = ({ handleUser }) => {
    const [username, setUsername] = useState('')
    const [error, setError] = useState(false)
    const [errorText, setErrorText] = useState('')

    const SignIn = async () => {
        try {
            const response = await fetch('/api/v1/user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'username': username
                })
            })

            if (response.ok) {
                console.log('Success: ' + response.status + ' - ' + response.statusText)
                setError(false)
            } else {
                throw new Error(response.statusText)
            }

            let { data } = await response.json()

            handleUser({
                id: data.id,
                username: data.username,
                state: true
            })

            console.log(data)

        } catch (e) {
            console.log(e)
            setError(true)
            setErrorText(e.message)
        }
    }

    const LogIn = async () => {
        try {
            const response = await fetch(`/api/v1/user?username=${username}`)

            if (response.ok) {
                console.log('Success: ' + response.status + ' - ' + response.statusText)
                setError(false)
            } else {
                throw new Error(response.statusText)
            }

            let { data } = await response.json()

            handleUser({
                id: data.id,
                username: data.username,
                state: true
            })

            console.log(data)

        } catch (e) {
            console.log(e)
            setError(true)
            setErrorText(e.message)
        }
    }

    return (
        <Container textAlign='center' style={{ margin: 'auto', paddingLeft: '25%', paddingRight: '25%' }}>
            <Message
                attached
                header='Welcome to our the greenhouse!'
                content='Fill out the form below to sign-up or log-in' />
            <Form className='attached fluid segment'>
                <Form.Field>
                    <label>Username</label>
                    <input placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
                </Form.Field>
                <FormField>
                    <Button.Group>
                        <Button onClick={SignIn}>SignIn</Button>
                        <Button.Or />
                        <Button primary onClick={LogIn}>LogIn</Button>
                    </Button.Group>
                </FormField>
            </Form>
            {error && <Message attached='bottom' error>
                <Icon name='database' />
                {errorText}
            </Message>}
        </Container>
    )
}

export default LogLogic