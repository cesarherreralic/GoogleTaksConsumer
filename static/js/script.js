/*Script for khan's task */


$(document).ready(function(){

	function load_json(){

		console.log('this actually will load something');
		console.log('by cesarherreralic');




	}

	function load_tasks(){

	    $.ajax({
          type: "GET",
          url: "https://www.googleapis.com/tasks/v1/lists/MDMyMDcwMjY4NTc2MzE0NDcyMTg6MDow/tasks",
          success: function(data){
              console.log(data);
          }
        });

	}


	load_json();




});