const hamburger = document.getElementById("hamburger");
const navlinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navlinks.classList.toggle("active");
}
const navLink = document.querySelectorAll(".nav-links>a");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navlinks.classList.remove("active");
}