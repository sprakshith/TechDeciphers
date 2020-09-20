$(document).ready(function() {

  $("#dropSuggestion").click(function(){
    $("#openDropSuggestionModal").modal();
  });

  $('#submitSuggestionButtom').click(function() {
      var flag = false;
      var email = $('#emailAddress').val();
      var suggestion = $('#suggestionText').val();

      if(email == "") {
        $('#emailAddress').css({'border-color' : 'red'});

        setTimeout(function() {
          $('#emailAddress').css({'border-color' : '#ced4da'});
        }, 2000);
      }

      if(suggestion == "") {
        $('#suggestionText').css({'border-color' : 'red'});

        setTimeout(function() {
          $('#suggestionText').css({'border-color' : '#ced4da'});
        }, 2000);
      }

      if(email != "" && suggestion != "") {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

        if(re.test(String(email).toLowerCase())) {
          flag = true;
        }
        else {
          $('#emailError').show();

          setTimeout(function() {
            $('#emailError').hide();
          }, 2000);
        }
      }

      if(flag) {
        $.ajax({
              url: '/dropSuggestion/',
              data: {
                'EMAILID': email,
                'SUGGESTION': suggestion
              },
              dataType:'json',
              success: function (data) {
                console.log(data.Message)
                $('#emailAddress').val("");
                $('#suggestionText').val("");
                $('#successMessage').show();

                setTimeout(function() {
                  $("#openDropSuggestionModal").modal('hide');
                  $('#successMessage').hide();
                }, 3000);
              }
        });
      }
  });

});
