var express = require('express')
var jquery = require('jquery');
var http = require('http');
var routes = require('./routes')
var fs = require('fs');
var path = require('path');

var app = express();


app.listen(8000, function () {
console.log("Express server listening on port 8000");
});

app.use('/accounts', accounts);


router.verb('/127.0.0.1:8000/users', function (req, res, next) {
});