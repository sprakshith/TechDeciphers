$(document).ready(function(){

  $('.navigationSearchBar').autoComplete({
    resolverSettings: {
        url: '/get_tutorials_heading/'
    }
  });

});


function myFunction() {
  var navigationLinks = document.getElementById("myLinks");
  if (navigationLinks.style.display === "block") {
    $('#techDeciphersHeading').css({'display' : 'block'});
    $("#myLinks").css({'display' : 'none'});
    $(".topnav").css({'height' : '2.3em'});
  }
  else {
    $('#techDeciphersHeading').css({'display' : 'none'});
    $("#myLinks").css({'display' : 'block'});
    $(".topnav").css({'height' : '16em'});
  }
}


function searchArticles() {
  location.href="/get_searched_article_content/?search_article_name=" + $("#search_article_name").val();
}
