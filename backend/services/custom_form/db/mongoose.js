const mongoose = require('mongoose');

mongoose.connect('mongodb://root:example@host.docker.internal:27017/customform', 
{
    useNewUrlParser: true,
    useUnifiedTopology: true
});