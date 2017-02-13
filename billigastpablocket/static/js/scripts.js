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
      	  $('#results').show();
          $('#result').text(data.search);
          $('#result-text').text(data.answer+"kr");
      }
    })
}