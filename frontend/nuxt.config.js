module.exports = {
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
    vendor: ['axios']
    // /*
    // ** Run ESLINT on save
    // */
    // extend (config, ctx) {
    //   if (ctx.isDev && ctx.isClient) {
    //     config.module.rules.push({
    //       enforce: 'pre',
    //       test: /\.(js|vue)$/,
    //       loader: 'eslint-loader',
    //       exclude: /(node_modules)/
    //     })
    //   }
    // }
  },
  serverMiddleware: [
    // API middleware
    '~/api/index.js'
  ]
}
