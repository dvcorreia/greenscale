const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = (env, argv) => ({
    entry: './src/index',
    output: {
        path: `${__dirname}/public`,
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Greenhouse',
            template: 'src/index.html'
        })
    ],
    devServer: {
        disableHostCheck: true,
        host: '0.0.0.0',
        port: 80
    },
    devtool: argv.mode === 'development' ? 'cheap-module-source-map' : false
})
