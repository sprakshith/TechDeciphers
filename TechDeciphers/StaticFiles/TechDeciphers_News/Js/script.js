function openThisArticle(articleId) {

  $('#articlePrimaryId').val(articleId);
  $('#getArticlePostContents').submit();

  // $.ajax({
  //       url: '/news/tryingAjaxCall/',
  //       data: {
  //         'primary_key': articleId
  //       },
  //       dataType:'json',
  //       success: function (data) {
  //         console.log(data)
  //       }
  // });

}
