$(function(){
	$(".check-flight").click(function(){
		$(this).next().removeClass("hidden");
		$(this).addClass("hidden");
			
		var bookingId = $(this).attr("booking-id");
		$.post("check-flight/"+bookingId,
			{csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},function(data){
				if(data.length>0){
					$("#collapse"+bookingId+" div.panel-body").html(data);	
				}
		});
	});
	
	$(".btn-danger").click(function(){
		$(".check-flight",$(this).parent()).toggleClass("hidden");
		$(this).toggleClass("hidden");
		var bookingId = $(this).attr("booking-id");

		$("#collapse"+bookingId+" div.panel-body").html($("#loader").clone().removeClass("hidden"));	
	});

	
	$("body").delegate("button.check-manual-flight","click",function(){
		var bookingId = $(this).attr("booking-id");
		var user_flight_number = $.trim($(this).prev().val());
		if (user_flight_number.length >4){
			$.post("check-flight/"+bookingId+"/"+user_flight_number,
				{csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},function(data){
					if(data.length>0){
						$("#collapse"+bookingId+" div.panel-body").html(data);	
					}
			});	
		}
	});

	$("body").delegate("button.save-flight-number","click",function(){
		var bookingId = $(this).attr("booking-id");
		$.post("save-flight-number/"+$(this).attr("booking-id")+"/"+$(this).attr("user-flight-number"),
			{csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},function(data){
				if(data=='ok'){
					$("#collapse"+bookingId+" div.panel-body").html("Flight number saved.");	
				}
				else{
					$("#collapse"+bookingId+" div.panel-body").html("There has been a problem saving the information. Please, close and try again.");
				}
		});	
	});

});