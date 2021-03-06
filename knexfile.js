require("dotenv").config();
module.exports = {
  development: {
    client: "mysql",
    connection: {
      port: process.env.DATABASE_PORT,
      host: process.env.DATABASE_HOST,
      database: process.env.DATABASE_NAME,
      user: process.env.DATABASE_USER,
      password: process.env.DATABASE_ACCESS_KEY
    },
    pool: {
      min: 2,
      max: 10
    }
  },

  testing: {
    client: "mysql",
    connection: {
      port: process.env.DATABASE_PORT,
      host: process.env.DATABASE_HOST,
      database: process.env.DATABASE_NAME,
      user: process.env.DATABASE_USER,
      password: process.env.DATABASE_ACCESS_KEY
    },
    pool: {
      min: 2,
      max: 10
    }
  },

  production: {
    client: "mysql",
    connection: {
      port: process.env.DATABASE_PORT,
      host: process.env.DATABASE_HOST_PRODUCTION,
      database: process.env.DATABASE_NAME,
      user: process.env.DATABASE_USER,
      password: process.env.DATABASE_ACCESS_KEY
    },
    pool: {
      min: 2,
      max: 10
    }
  }
};
