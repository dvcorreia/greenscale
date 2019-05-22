import React, { useState } from 'react'
import { Form, Button, FormField, Grid, Message, Icon } from 'semantic-ui-react'


const LogLogic = ({ setUser }) => {
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
                console.log('User endpoint (SignIn)[success]: ' + response.status + ' - ' + response.statusText)
                setError(false)
            } else {
                throw new Error(response.statusText)
            }

            let { data } = await response.json()

            setUser({
                id: data.id,
                username: data.username,
                greenhouses: data.greenhouses,
                state: true
            })

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
                console.log('User endpoint (LogIn)[success]: ' + response.status + ' - ' + response.statusText)
                setError(false)
            } else {
                throw new Error(response.statusText)
            }

            let { data } = await response.json()

            setUser({
                id: data.id,
                username: data.username,
                greenhouses: data.greenhouses,
                state: true
            })

        } catch (e) {
            console.log(e)
            setError(true)
            setErrorText(e.message)
        }
    }

    return (
        <Grid centered columns={1}>
            <Grid.Column width={12} textAlign='center'>
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
                            <Button primary onClick={LogIn}>LogIn</Button>
                            <Button.Or />
                            <Button onClick={SignIn}>SignIn</Button>
                        </Button.Group>
                    </FormField>
                </Form>
                {error && <Message attached='bottom' error>
                    <Icon name='database' />
                    {errorText}
                </Message>}
            </Grid.Column>
        </Grid>
    )
}

export default LogLogic