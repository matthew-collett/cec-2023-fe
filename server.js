/* server.js */

/* imports */
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const { callPython } = require('./py-caller')

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

    body = await callPython(path.join(__dirname, 'public/scripts/test.py'));

    // render the page 
    res.render(path.join(__dirname, '/client/index'), body);
});

app.get('/sign-in', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/actions/sign-in');
});

app.get('/create-account', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/actions/create-account');
});

app.get('/equally', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/equally');
});

app.get('/proportion', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/proportion');
});

app.get('/urgency', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/urgency');
});

app.get('/distribution', async function (req, res) {
    // render the page 
    res.render(__dirname + '/client/distribution');
});