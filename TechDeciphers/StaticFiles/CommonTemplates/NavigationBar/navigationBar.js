function myFunction() {
  var navigationLinks = document.getElementById("myLinks");
  if (navigationLinks.style.display === "block") {
    $("#myLinks").css({'display' : 'none'});
  }
  else {
    $("#myLinks").css({'display' : 'block'});
  }
}
