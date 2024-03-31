require('./db/mongoose');
const express = require("express");
const customform = require('./models/customform');

const app = express();

app.set('view engine', 'ejs');

app.use(express.json());
app.use(express.static('public'));

app.post('/form', (req, res) => {
    const recommendations = new customform(req.body);
    recommendations.save().then((customform) => {
        res.status(201).send(customform);
    }).catch((error) => {
        res.status(400).send(error);
    })
});

app.get('/form', (req, res) => {
    customform.find({}).then((form) => {
        res.send(form);
    }).catch((error) => {
        res.status(500).send(error);
    })
});

app.get('/form/:date&:flight', (req, res) => {
    customform.findOne({date: req.params.date, flight_id: req.params.flight}).then((form) => {
        if (!form) {
            return res.status(404).send();
        }
        res.render('form', { date: form.date, flight_id: form.flight_id, recommended_flights: form.recommended_flights, recommended_accommodation: form.recommended_accommodation });
    }).catch((error) => {
        res.status(500).send(error);
    })
});

app.listen(4545, () => {
    console.log("--- Custom Form Service is running ---")
});