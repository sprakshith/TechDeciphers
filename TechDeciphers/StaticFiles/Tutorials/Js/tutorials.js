$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip()
})

function openThisArticle(articleId) {
  $('#article_primary_id').val(articleId);
  $('#get_article_post_contents').submit();
}
