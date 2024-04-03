require('./db/mongoose');
const express = require("express");
const bodyParser = require("body-parser");
const customform = require('./models/customform');
const Producer = require('./producer');
const producer = new Producer();

const app = express();

app.set('view engine', 'ejs');

app.use(express.json());
app.use(express.static('public'));
app.use(bodyParser.json("application/json"));

app.post('/form', (req, res) => {
    const recommendations = new customform(req.body);
    recommendations.save().then(async(customform) => {
        res.status(201).send(customform);
        for (let mail of req.body.user_emails){
            let temp_email = mail.email;
            let pax = mail.pax;
            console.log(pax)
            const message = `http://localhost:5012/form/${req.body.departure}&${req.body.flight_number}&${temp_email}&${pax}`;
            await producer.publishMessage('form.notifications', temp_email , "Rebook Flight", message);
            res.send();
        }
    }).catch((error) => {
        res.status(400).send(error);
    })
});

// app.get('/form', (req, res) => {
//     customform.find({}).then((form) => {
//         res.send(form);
//     }).catch((error) => {
//         res.status(500).send(error);
//     })
// });

app.get('/form/:departure&:flight_number&:email&:pax', (req, res) => {
    customform.findOne({departure: req.params.departure, flight_number: req.params.flight_number}).then((form) => {
        if (!form) {
            return res.status(404).send();
        }
        res.render('form', { id:form._id, departure: form.departure, flight_number: form.flight_number, recommended_flights: form.recommended_flights, recommended_accommodation: form.recommended_accommodation, email: req.params.email, pax: req.params.pax});
    }).catch((error) => {
        res.status(500).send(error);
    })
});

app.post('/sendform', async(req, res, next) => {
    await producer.publishMessage('notifications', req.body.email, req.body.notification_type, req.body.notification_message);
    res.send();
})

app.listen(5012, () => {
    console.log("--- Custom Form Service is running ---")
});