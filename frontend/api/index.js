const express = require('express');
const passport = require('passport');
const passportConfig = require('./passport');
const { sequelize } = require('./models/index');

// Create express instnace
const app = express();
passportConfig();
sequelize.sync();

// Require API routes
const users = require('./routes/users');
const server = require('./routes/server');

// Middlewares
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(passport.initialize());
app.use(passport.session());

// Import API Routes
app.use(users);
app.use(server);

// Export the server middleware
module.exports = {
  path: '/api',
  handler: app
};
