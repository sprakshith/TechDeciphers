$(document).ready(function(){

  $('[data-toggle="tooltip"]').tooltip()

});

function openThisArticle(article_id, article_type) {
  $('#article_primary_id').val(article_id);
  $('#article_type').val(article_type);
  $('#get_article_post_contents').submit();
}
