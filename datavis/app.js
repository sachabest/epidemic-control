var express = require('express');
var vis = require('vis');
var app = express();

app.set('view engine', 'jade');

app.get('/', function (req, res) {
	res.render("index");
});

app.get('main.js', function (req, res) {
	res.sendFile('main.js');
});

app.get('vis.js', function (req, res0 ){
	res.sendFile('node_modules/vis/dist/vis.min.js');
});

app.get('vis.css', function (req, res0 ){
	res.sendFile('node_modules/vis/dist/vis.min.css');
});

var server = app.listen(80, function () {

	var host = server.address().address;
	var port = server.address().port;

	console.log('Example app listening at http://%s:%s', host, port);

});
