var container = Documet.getElementById('container');

var gephiJSON = loadJSON("gephi.json");
var data = { gephi: gephiJSON };
var network = new vis.Network(container, data);