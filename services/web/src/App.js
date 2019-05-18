import React from 'react';
import MainWindow from './Components/MainWindow'
import { Container } from 'semantic-ui-react'

const App = () => {
  const [user, setUser] = React.useState({
    id: '',
    username: '',
    greenhouses: [],
    state: false
  })


  return (
    <div style={{ margin: 15 }}>
      <MainWindow user={user} setUser={setUser} />
    </div>
  );
}

export default App;
