function myFunction() {
  var navigationLinks = document.getElementById("myLinks");
  if (navigationLinks.style.display === "block") {
    $('#techDeciphersHeading').css({'display' : 'block'});
    $("#myLinks").css({'display' : 'none'});
    $(".topnav").css({'height' : '40px'});
  }
  else {
    $('#techDeciphersHeading').css({'display' : 'none'});
    $("#myLinks").css({'display' : 'block'});
    $(".topnav").css({'height' : '270px'});
  }
}
