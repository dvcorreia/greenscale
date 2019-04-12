import React from 'react'

class App extends React.Component {
    handleClick = e => console.log('Clicked')

    render() {
        return (
            <div>
                <h2>Click me and check the console</h2>
                <button onClick={this.handleClick}>Click</button>
            </div>
        )
    }
}

export default App
