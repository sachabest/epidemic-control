var timesteps;
var colors = ["#FFFDB2", "#FF8F87", "#9FFF78"];

function updateNodes(s, timesteps, value) {
	for (var node = s.graph.nodes().length - 1; node >= 0; node--) {
		var nodeprop = s.graph.nodes()[node];
		var id = nodeprop.id;
		nodeprop.color = colors[timesteps[id][value]];
		//nodeprop.originalColor = colors[timesteps[id][time]];;
	}
	s.refresh();
}

$(document).ready(function() {
	$('#play').prop('disabled', true);
	var graph;
	sigma.parsers.gexf('sample.gexf', { container: 'sigma'}, function(s) {
		graph = s.graph;
		s.settings("maxNodeSize", 4);
		// this to fix a bug where the first node is not modified		
		$('#timestep').change(function () {
			var time = $(this).val();
			updateNodes(s, timesteps, time);
		});

		var playing = false;
		var i = 1;                  	//  set your counter to 1
		function play () {        	//  create a loop function
	  		setTimeout(function () {    //  call a 3s setTimeout when the loop is called
				$('#timestep').val(i);
				$('#timestep').change();
				if (playing) {
					i++;                    //  increment the counter
		      		if (i < 60) {           //  if the counter < 10, call the loop function
		         		play();           //  ..  again which will trigger another 
		      		} else {
		      			$('#play').text('Reset');
		      			playing = false;
		      		}
		      	}
	   		}, 200)
		} 
		$('#play').click(function () {
			// reset case
			if (i >= 60) {
				i = 1;
				$('#timestep').val(i);
				$('#timestep').change();
				$('#play').text('Play');
				return;
			}
			// play case
			if (!playing) {
				playing = true;
				play();
				$('#play').text('Playing (click to stop)');
				$('#play').parent().addClass('active');
			}
			// stop case
			else {
				playing = false;
				$('#play').text('Play');
			}
		});
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
		    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
		        timesteps = JSON.parse(xmlhttp.responseText);
				$('#play').prop('disabled', false);
				$('#play > span').text("Play");
				updateNodes(s, timesteps, 0);
		   	}	
		};
		xmlhttp.open("GET", 'states.json', true);
		xmlhttp.send();
	});

});