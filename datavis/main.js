$(document).ready(function() {
	var xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var data = JSON.parse(xmlhttp.responseText);
	        console.log('json back');
			var container = document.getElementById('container');
			var parserOptions = {
				allowedToMove: false,
				parseColor: false
			};
			var parsed = vis.network.gephiParser.parseGephi(data, parserOptions);
			var options = {
				width:  '100%',
				height: '400px',
				edges: {
					color: 'red',
					width: 2
				},
				//hierarchicalLayout: true
			};
			var data = {
			  	nodes: parsed.nodes,
			  	edged: parsed.edges
			};
			var network = new vis.Network(container, data, options);

	   	}	
	};

	xmlhttp.open("GET", 'gephi.json', true);
	xmlhttp.send();
`