const passport = require('passport');
const localStrategy = require('./localStrategy');
const { User } = require('../models');

module.exports = () => {
  passport.serializeUser((user, done) => {
    done(null, user.id);
  });

  passport.deserializeUser(async (id, done) => {
    const brand = await User.find({ where: { id } });
    done(null, brand);
  });

  localStrategy(passport);
};
