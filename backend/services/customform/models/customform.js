const mongoose = require('mongoose');

const customFormSchema = new mongoose.Schema({
    date: String,
    flight_id: String,
    recommended_flights: [{date: String, flight_id: String, availability: Number}],
    recommended_accommodation: [{hotel_name: String, availability: Number}],
    user_emails: Array,
});

const customform = mongoose.model('customform', customFormSchema);

module.exports = customform;