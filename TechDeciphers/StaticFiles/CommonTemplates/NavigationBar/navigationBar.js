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
