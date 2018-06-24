module.exports = (sequelize, Sequelize) => (
  sequelize.define('user', {
    email: {
      type: Sequelize.STRING(50),
      allowNull: false,
    },
    password: {
      type: Sequelize.STRING(100),
      allowNull: false,
    },
    name: {
      type: Sequelize.STRING(20),
      allowNull: false,
    },
    phone: {
      type: Sequelize.STRING(15),
      allowNull: false,
    },
  }, {
    timestamps: true,
    comment: '회원 정보',
    charset: 'utf8',
    collate: 'utf8_unicode_ci',
  })
);
