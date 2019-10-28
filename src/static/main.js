$(function() {
    $.ajax({
        url: '/api/info',
        success: function(data) {
            console.log('get info');
            $('#info').html(JSON.stringify(data, null, '   '));
            $('#description').html(data['description']);
        }
    });


    var message = JSON.stringify({ "message":"Porsche" });

    console.log(message)
    $.ajax({
      url: '/api/hi',
      type: 'POST',
      ContentType: 'application/json',
      data:  message
    }).done(function(response){
      console.log('success');
    }).fail(function(jqXHR, textStatus, errorThrown){
      console.log('FAILED! ERROR: ' + errorThrown);
    });
    $('#calc').click(function() {
        $('#info').css('display', "none");
        $('#description').css('display', "none");
        console.log("url");
        $.ajax({
            url : '/api/calc?a=' + document.getElementById('a').value + '&b=' + document.getElementById('b').value,
            success: function(data) {
                $('#add').html(data['a'] + ' + ' + data['b'] + ' = ' + data['add']);
                $('#subtract').html(data['a'] + ' - ' + data['b'] + ' = ' + data['subtract']);
                $('#multiply').html(data['a'] + ' * ' + data['b'] + ' = ' + data['multiply']);
                $('#divide').html(data['a'] + ' / ' + data['b'] + ' = ' + data['divide']);
            }
        });
    });
})