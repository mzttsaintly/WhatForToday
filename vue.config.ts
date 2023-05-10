module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1/',
                ws: true,
                changeOrigin: true,
                secure: true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    }
}