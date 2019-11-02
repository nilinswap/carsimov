$(function() {
    $.ajax({
        url: '/api/hi_from_python',
        success: function(data) {
            $('#from_python').html("hi " + data['name'] + ", this is Javeh. (sent by python)");
        }
    });


    var message = JSON.stringify({ "name":"Javeh" })

    console.log(message)
    $.ajax({
      url: '/api/hi_from_js',
      type: 'POST',
      ContentType: 'application/json;charset=UTF-8',
      data:  message
    }).done(function(response){
      console.log('success');
      console.log(response)
      //data = JSON.parse(response)

      $('#from_js').html( response['message'] + ". (sent by js)" );

    }).fail(function(jqXHR, textStatus, errorThrown){
      console.log('FAILED! ERROR: ' + errorThrown);
    });

})