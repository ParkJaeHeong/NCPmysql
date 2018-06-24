const express = require('express')

// Create express instnace
const app = express()

// Require API routes
const users = require('./routes/users')
const server = require('./routes/server')

// Import API Routes
app.use(users)
app.use(server);

// Export the server middleware
module.exports = {
  path: '/api',
  handler: app
}
