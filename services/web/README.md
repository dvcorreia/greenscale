# Web

This service provides a __web interface__ to interact with the platform. This allows the user to see the sensor's telemetry and add greenhouses, beds and sensors.

## Development

This web application if fully built on [React JS](https://reactjs.org/), a JavaScript library for building user interfaces. It was also started with [create-react-app](https://github.com/facebook/create-react-app) boilerplate by the React creators, which is Facebook. 

So to start a development environment you can go to the root directory of the project and type in the terminal `yarn start` (this also means you have to have [yarn](https://yarnpkg.com/) or [npm](https://www.npmjs.com/) installed, __npm__ comes bundled with [Node JS](https://nodejs.org/)).
To compile a production build you can run `yarn build`. 

The UI components were all sourced from a library and UI framework called [Semantic UI](https://semantic-ui.com/). Semantic UI has a version built with React components that can be checked [here](https://react.semantic-ui.com/) and which is used in this application.

The graphs were build using a [d3.js](https://d3js.org/) react wrapper called [VX](https://vx-demo.now.sh/).

## Pipeline build

On production environment of the platform, the web application is built in a Node JS image and then copied to an image of [NGINX](https://www.nginx.com/) and served has static files con port 80.

