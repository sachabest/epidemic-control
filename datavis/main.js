var timesteps;
var colors = ["#FFFDB2", "#FF8F87", "#9FFF78"];

$(document).ready(function() {
	$('#play').prop('disabled', true);
	var graph;
	sigma.parsers.gexf('sample.gexf', { container: 'sigma'}, function(s) {
		graph = s.graph;
		console.log(graph);

		$('#timestep').change(function () {
			var time = $(this).val();
			console.log(time);
			for (var node = 1; node < graph.nodes().length; node++) {
				var nodeprop = graph.nodes()[node];
				var id = nodeprop.id;
				nodeprop.color = colors[timesteps[id][time]];
				nodeprop.originalColor = colors[timesteps[id][time]];;
			}
			s.refresh();
		});

		$('#play').click(function () {
			for (var i = 1; i < 1000; i++) {
				setTimeout( function() {
					for (var node = 1; node < graph.nodes().length; node++) {
						var nodeprop = graph.nodes()[node];
						var id = nodeprop.id;
						nodeprop.color = colors[timesteps[id][i]];
					}
				}, 250);
			}
		});
	});
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        timesteps = JSON.parse(xmlhttp.responseText);
	        console.log('json back');
			$('#play').prop('disabled', false);
	   	}	
	};
	xmlhttp.open("GET", 'states.json', true);
	xmlhttp.send();
	
});



