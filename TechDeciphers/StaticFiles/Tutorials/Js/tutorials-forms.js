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
  
});
