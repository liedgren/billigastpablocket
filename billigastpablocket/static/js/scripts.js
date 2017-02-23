function submitSearch(){
	$.ajax({
	  type: 'POST',
      url: "/getSearch/",
      data: {
        "csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val(),
        "search" : $("#searchTerm").val()
      },
      cache: false,
      success: function(data){
      	  data = JSON.parse(data);
      	  if(data.errorResult == 'no-result'){
  	      	$('#results').hide();
      	  	$('#error').show();
      	  }
      	  else{
      	 	 $('#results').show();
          	//$('#result').text(data.search);
            $('#result-text-1').text(data.min+"kr");
          	$('#result-text-2').text(data.med+"kr");
            $('#result-text-3').text(data.max+"kr");
          	$('#error').hide();
      	  }
      }
    })
}