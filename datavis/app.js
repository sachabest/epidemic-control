var express = require('express');
var vis = require('vis');
var app = express();

app.set('view engine', 'jade');

app.get('/', function (req, res) {
	res.render("index");
});

app.get('/main.js', function (req, res) {
	res.sendFile('main.js', {root: '.'});
});

app.get('/main.css', function (req, res) {
	res.sendFile('main.css', {root: '.'});
});

app.get('/vis.js', function (req, res ){
	res.sendFile('node_modules/vis/dist/vis.js', {root: '.'});
});

app.get('/vis.css', function (req, res ){
	res.sendFile('node_modules/vis/dist/vis.css', {root: '.'});
});

app.get('/vis.map', function (req, res ){
	res.sendFile('node_modules/vis/dist/vis.map', {root: '.'});
});

app.get('/gephi.json', function (req, res ){
	res.sendFile('gephi.json', {root: '.'});
});

var server = app.listen(8080, function () {

	var host = server.address().address;
	var port = server.address().port;

	console.log('Example app listening at http://%s:%s', host, port);

});
