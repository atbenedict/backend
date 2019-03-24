const knex = require("knex");
const knexConfig = require("../../knexfile");
const db = knex(knexConfig.development);
module.exports = {
  getAllIncidents: function() {
    return db("data");
  },
  getIncidentById: function(id) {
    return db("data")
      .where({ incident_id: id })
      .first();
  },
  getIncidentByState: function(state) {
    return db("data").where({ state: state });
  }
};
