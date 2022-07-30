$(document).ready(function() {

  $('#id_content').summernote({
      toolbar: [
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['font', ['strikethrough']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture']],
        ['view', ['codeview']],
      ]
  });

  $('.note-editable').css({'height':'400px','background-color':'white'});

  $('.form-datepicker').flatpickr();

  $('#id_isChildPage').change(function() {
    if($("#id_isChildPage").is(":checked")) {
      $(".child-tutorial-information").show();
    }
    else {
      $(".child-tutorial-information").hide();
      $("select.form-control").val(0);
    }
  });

  $("#select-parent-id").change(function(){
     $.ajax({
            type: "GET",
            url: '/tutorials/fetch_previous_next_tutorials',
            data: {
              'PARENT_ARTICLE_ID': $(this).val()
            },
            dataType:'json',
            success: function (data) {
              $("#select-previous-post-id").html('<option value="0">No Previous Post</option>');
              $("#select-next-post-id").html('<option value="0">No Next Tutorial</option>');

              var child_tutorials = data.child_tutorials;

              for(var index in child_tutorials) {
                  var htmlContent = '<option value="'+ child_tutorials[index]["TUTORIAL_ID"] +'">'+ child_tutorials[index]["TUTORIAL_NAME"] +'</option>';
                  $("#select-previous-post-id, #select-next-post-id").append(htmlContent);
              }
            }
      });
  });

});
