$(document).ready(function() {

  $('#keepMeUpdatedBtn').click(function() {
    var flag = false;
    var emailIdVal = $('#stayConnected input').val();

    if(emailIdVal != "") {
      const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

      if(re.test(String(emailIdVal).toLowerCase())) {
        flag = true;
      }

      if(flag) {
        $.ajax({
              url: '/keepMeUpdated/',
              data: {
                'EMAILID': emailIdVal,
              },
              dataType:'json',
              success: function (data) {
                console.log(data.Message)
                $('#stayConnected input').val("");
              }
        });
      }
    }

  });

});
