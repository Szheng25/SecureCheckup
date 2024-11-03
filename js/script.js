/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function hamburger() {
    var nav = document.getElementById("nav");
    if (nav.style.display === "block") {
        nav.style.display = "none";
    } else if (nav.style.display === "") {
        nav.style.display = "none";
    } else {
        nav.style.display = "block";
    }
}
