import React from 'react'

class App extends React.Component {
    handleClick = e => console.log('Clicked')

    render() {
        return <button onClick={this.handleClick}>Click</button>
    }
}

export default App
