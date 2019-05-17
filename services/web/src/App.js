import React from 'react';
import MainWindow from './Components/MainWindow'
import { Container } from 'semantic-ui-react'

const App = () => {
  const [user, handleUser] = React.useState({
    id: '',
    username: '',
    state: false
  })


  return (
    <Container style={{ marginTop: 20 }}>
      <MainWindow user={user} handleUser={handleUser} />
    </Container>
  );
}

export default App;
