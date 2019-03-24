const express = require("express");
const knex = require("knex");
const router = express.Router();
const helper = require("../helpers/gunDataHelpers");

router.get("/:id", (req, res) => {
  const id = req.params.id;
  helper
    .getIncidentById(id)
    .then(incident => {
      res.status(200).json(incident);
    })
    .catch(err => {
      res
        .status(500)
        .json({ errorMessage: `'error retrieving incident' ${err}` });
    });
});

router.get("/state/:state", (req, res) => {
  const state = req.params.state;
  helper
    .getIncidentByState(state)
    .then(incident => {
      res.status(200).json(incident);
    })
    .catch(err => {
      res
        .status(500)
        .json({ errorMessage: `'error retrieving incident' ${err}` });
    });
});

module.exports = router;
