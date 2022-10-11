// ----------------- Toggle Dark Mode ----------------- //
let toggle = document.getElementById("dark-mode-toggle");
let root = document.querySelector(':root');
const change_theme = ()=>{
  // TODO: Fix tooltip not updating
  if(toggle.childNodes[1].childNodes[1].childNodes[0].getAttribute("data-icon") == "akar-icons:sun"){
    toggle.childNodes[1].childNodes[1].childNodes[0].setAttribute("data-icon", "bi:moon");
    root.style.setProperty('--body-bg','#20242C');
    // root.style.setProperty('--navbar-bg','#3F72AF');
    root.style.setProperty('--btn-bg','#3F72AF');
    root.style.setProperty('--content-bg','#2A303C');
    root.style.setProperty('--text-component','#E5E9f0');
    root.style.setProperty('--text-body','#E5E9f0');
    localStorage.setItem('theme','dark');
    toggle.setAttribute("title", "Switch To Light Mode");
  }
  else{
    toggle.childNodes[1].childNodes[1].childNodes[0].setAttribute("data-icon", "akar-icons:sun");
    root.style.setProperty('--body-bg','#F0F4FB');
    // root.style.setProperty('--navbar-bg','#3F72AF');
    root.style.setProperty('--btn-bg','#112D4E');
    root.style.setProperty('--content-bg','#DBE2EF');
    root.style.setProperty('--text-component','#E5E9F0');
    root.style.setProperty('--text-body','#111318');
    localStorage.setItem('theme','light');
    toggle.setAttribute("title", "Switch To Dark Mode");
  }
};
if (localStorage.getItem('theme') != null){
  let thm = localStorage.getItem('theme');
  if (thm == 'dark'){
    toggle.childNodes[1].childNodes[1].childNodes[0].setAttribute("data-icon", "akar-icons:sun"); 
  }
  else{
    toggle.childNodes[1].childNodes[1].childNodes[0].setAttribute("data-icon", "bi:moon");
  } 
  change_theme();
}
toggle.addEventListener('click', change_theme);

// navbar
var mediaQuery = window.matchMedia("(max-width: 991.49px)");
if (mediaQuery.matches) {
  document.getElementById("iconifyEditProfile").innerHTML =
    '<span class="iconify iconify-navbar" data-icon="akar-icons:edit" data-width="28" data-height="28"></span> Edit Profile';
  document.getElementById("iconifyNotification").innerHTML =
    '<span class="iconify iconify-navbar" data-icon="clarity:notification-solid" data-width="27" data-height="28"></span> Notification';
  document.getElementById("iconifyMessage").innerHTML =
    '<span class="iconify iconify-navbar" data-icon="bx:message-detail" data-width="26" data-height="28"></span> Message';
  document.getElementById("iconifyLogOut").innerHTML =
    '<span class="iconify iconify-navbar" data-icon="ic:outline-log-in" data-width="27" data-height="27"></span> Log Out';

  document.getElementById("iconifyEditProfile").style.color = "white";
  document.getElementById("iconifyNotification").style.color = "white";
  document.getElementById("iconifyMessage").style.color = "white";
  document.getElementById("iconifyLogOut").style.color = "white";

  document.getElementById("iconifyEditProfile").style.textShadow =
    "0 0 2px rgb(0 0 0)";
  document.getElementById("iconifyNotification").style.textShadow =
    "0 0 2px rgb(0 0 0)";
  document.getElementById("iconifyMessage").style.textShadow =
    "0 0 2px rgb(0 0 0)";
  document.getElementById("iconifyLogOut").style.textShadow =
    "0 0 2px rgb(0 0 0)";
}

// Tooltip
var mediaQuery = window.matchMedia("(min-width: 991.49px)");
if (mediaQuery.matches) {
  (function () {
    "use strict";
    var tooltipTriggerList = [].slice.call(
      document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );

    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl);
    });
  })();
}

