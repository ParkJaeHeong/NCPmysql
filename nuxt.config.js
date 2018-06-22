const webpack = require('webpack')

module.exports = {
  /*
  ** Router config
  */
  router: {
    middleware: [ 'check-auth' ]
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'NAVER CLOUD PLATFORM',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', type: 'text/css', href: 'http://cdn.jsdelivr.net/font-nanum/1.0/nanumbarungothic/nanumbarungothic.css' }
    ]
  },
  loading: {
    color: '#14adea'
  },
  /*
  ** Global CSS
  */
  css: [
    {src: '~/assets/less/app.less', lang: 'less'}
  ],
  /*
  ** Add axios globally
  */
  build: {
    vendor: [
      'axios',
      'vee-validate'
    ],
    plugins: [
      new webpack.ProvidePlugin({
        '$': 'jquery',
        jQuery: 'jquery'
      })
    ],
    /*
    ** Run ESLINT on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  plugins: [
    {src: '~/plugins/vee-validate.js'},
    {src: '~/plugins/vue-authenticate.js', ssr: false}
  ]
}
