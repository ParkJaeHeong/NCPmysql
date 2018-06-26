const { Router } = require('express');
const bcrypt = require('bcrypt');
const passport = require('passport');
const { User } = require('../models');

const router = Router();

// Mock Users
const users = [
  { name: 'Alexandre' },
  { name: 'Pooya' },
  { name: 'Sébastien' }
];

/* GET users listing. */
router.get('/users', function (req, res, next) {
  res.json(users)
});

/* GET user by ID. */
router.get('/users/:id', function (req, res, next) {
  const id = parseInt(req.params.id);
  if (id >= 0 && id < users.length) {
    res.json(users[id])
  } else {
    res.sendStatus(404)
  }
});

router.post('/users', async (req, res, next) => {
  try {
    const password = await bcrypt.hash(req.body.password, 12);
    const user = await User.create({
      email: req.body.email,
      password,
      name: req.body.name,
      phone: req.body.phone,
    });
    res.json(user);
  } catch (error) {
    console.log(error);
    next(error);
  }
});

router.post('/login', (req, res, next) => {
  passport.authenticate('local', (error, user, info) => {
    if (error) {
      console.error(error);
      return next(error);
    }
    if (info) {
      return res.status(403).json(info);
    }
    return req.login(user, (err) => {
      if (err) {
        console.error(err);
        return next(err);
      }
      return res.send('ok');
    });
  })(req, res, next);
});

module.exports = router;
