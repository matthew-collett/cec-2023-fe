/* server.js */

/* imports */
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const { callPython } = require('./public/scripts/py_caller')

const port = 3000;

/* app */
const app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});

/* main page */
app.get('/', async function (req, res) {

    body = await callPython("driver.py");
   
    // render the page 
    res.render(__dirname + '/client/index', body);
});