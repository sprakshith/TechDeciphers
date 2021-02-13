$(document).ready(function(){

  $('[data-toggle="tooltip"]').tooltip()

});

function openThisArticle(articleId, articleType) {

  $('#articlePrimaryId').val(articleId);
  $('#articleType').val(articleType);
  $('#getArticlePostContents').submit();

}
