const { Strategy } = require('passport-local');
const bcrypt = require('bcrypt');
const { User } = require('../models');
module.exports = (passport) => {
  passport.use(new Strategy({
    usernameField: 'email',
    passwordField: 'password',
  }, async (email, password, done) => {
    try {
      const user = await User.find({ where: { email } });
      if (!user) {
        return done(null, false, { message: '등록되지 않은 사용자입니다.' });
      }
      const result = await bcrypt.compare(password, user.password);
      if (!result) {
        return done(null, false, { message: '이메일과 비밀번호 조합이 맞지 않습니다.' });
      }
      return done(null, user);
    } catch (error) {
      console.error(error);
      return done(error);
    }
  }));
};
