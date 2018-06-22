import axios from '~/plugins/axios'

export default async (context) => {
  if (context.isServer && !context.req) return
  const userCookie = context.isServer ? getUserFromCookie(context.req) : context.app.router.app.$auth.getToken()
  if (!userCookie) {
    if (getNaviGuard(context.route)) return
    return context.redirect('/')
  }
  if (getNaviGuard(context.route)) return context.redirect('/provider/company')
  let data = await getUserInfo(userCookie)
  context.qsToken = userCookie
  context.store.commit('SET_USER', data)
}

const getUserFromCookie = (req) => {
  if (!req.headers.cookie) return
  const cookie = req.headers.cookie.split(';').find(c => c.trim().startsWith('qs_p'))
  if (!cookie) return
  return cookie.split('=')[1]
}

const getNaviGuard = (route) => {
  return route.name.match(/(index|member-register)/)
}

const getUserInfo = async (cookie) => {
  let { data } = await axios.get('/api/me', {
    headers: { 'Authorization': `Bearer ${cookie}` }
  })
  return data
}
