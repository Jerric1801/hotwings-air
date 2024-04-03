const mongoose = require('mongoose');

const customFormSchema = new mongoose.Schema({
    departure: String,
    flight_number: String,
    recommended_flights: [{departure: String, flight_number: String, availability: Number}],
    recommended_accommodation: [{hotel_name: String, availability: Number}],
    user_emails: Array,
});

const customform = mongoose.model('customform', customFormSchema);

module.exports = customform;