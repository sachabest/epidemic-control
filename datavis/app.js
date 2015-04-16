var express = require('express');
var vis = require('vis');
var app = express();

app.set('view engine', 'jade');

app.get('/', function (req, res) {
	res.render("index");
});

var server = app.listen(80, function () {

	var host = server.address().address;
	var port = server.address().port;

	console.log('Example app listening at http://%s:%s', host, port);

});
