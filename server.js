require("dotenv").config();
const cors = require("cors");
const helmet = require("helmet");
const express = require("express");
const server = express();

const auth = require("./api/routes/authRouter");
const gunDataRoute = require("./api/routes/gunDataRouter");

server.use(helmet());
server.use(express.json());
server.use(cors());
server.use("/api/user", auth);
server.use("/api/gundata", gunDataRoute);
server.get("/", (req, res) => {
  res.send("We are Live");
});

module.exports = server;
