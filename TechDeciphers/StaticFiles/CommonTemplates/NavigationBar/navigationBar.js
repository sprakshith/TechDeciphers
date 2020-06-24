function myFunction() {
  var navigationLinks = document.getElementById("myLinks");
  if (navigationLinks.style.display === "block") {
    $("#myLinks").css({'display' : 'none'});
    $(".topnav").css({'height' : '40px'});
    console.log("Hide Navigation Bar");
  }
  else {
    $("#myLinks").css({'display' : 'block'});
    $(".topnav").css({'height' : '235px'});
    console.log("Show Navigation Bar");
  }
}
