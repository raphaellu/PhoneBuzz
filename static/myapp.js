var validate_num = function(str){
	if (str == '') return 0		// set empty string as 0
    res = parseInt(str)
	if (str != (res+"") || res < 0) return -1;	// return -1 for invalid string or negative num
	else return res
}

$(function() {
    $('#submit').bind('click', function() {
      hours = validate_num($('input[name="hours"]').val())
      minutes = validate_num($('input[name="minutes"]').val())
      seconds = validate_num($('input[name="seconds"]').val())
      
      // only show info of scheduled time if time is entered 
      if (hours > 0 || minutes > 0 || seconds > 0 ) {
      	$('#scheduled_info').addClass("alert-info");
      	$('#scheduled_info').text("Scheduled the call in " + hours + 
      		" hour(s) " + minutes + " minute(s) " + seconds + " seconds.");
      	$('#scheduled_info').show();
      	$('.status_msg').hide();

      	$('#submit').hide();    // replace the submit button with a disabled submit button 
      	$('#submit_2').show();  // without affecting the http request
      }
    });
  });
