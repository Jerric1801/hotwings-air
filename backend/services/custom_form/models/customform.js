const mongoose = require('mongoose');

const customFormSchema = new mongoose.Schema({
    departure: String,
    flight_number: String,
    recommended_flights: [{flight_id: String, departure: String, flight_number: String, availability: Number}],
    recommended_accommodation: [{room_id: String, hotel_name: String, availability: Number}],
    user_emails: [{email: String, pax: Number}],
});

const customform = mongoose.model('customform', customFormSchema);

module.exports = customform;