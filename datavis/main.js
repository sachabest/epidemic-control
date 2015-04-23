$(document).ready(function() {

	sigma.parsers.gexf('sample.gexf', { container: 'sigma'}, function() {

	});
	var xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var data = JSON.parse(xmlhttp.responseText);
	        console.log('json back');

	   	}	
	};

	xmlhttp.open("GET", 'gephi.json', true);
	xmlhttp.send();
});