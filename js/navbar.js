// navbar
var mediaQuery = window.matchMedia('(max-width: 991.49px)')
if (mediaQuery.matches) {
  document.getElementById("iconifyEditProfile").innerHTML='<span class="iconify iconify-navbar" data-icon="akar-icons:edit" data-width="28" data-height="28"></span> Edit Profile'
  document.getElementById("iconifyNotification").innerHTML='<span class="iconify iconify-navbar" data-icon="clarity:notification-solid" data-width="27" data-height="28"></span> Notification'
  document.getElementById("iconifyMessage").innerHTML='<span class="iconify iconify-navbar" data-icon="bx:message-detail" data-width="26" data-height="28"></span> Message'
  document.getElementById("iconifyLogOut").innerHTML='<span class="iconify iconify-navbar" data-icon="ic:outline-log-in" data-width="27" data-height="27"></span> Log Out'

  document.getElementById("iconifyEditProfile").style.color="white"
  document.getElementById("iconifyNotification").style.color="white"
  document.getElementById("iconifyMessage").style.color="white"
  document.getElementById("iconifyLogOut").style.color="white"

  document.getElementById("iconifyEditProfile").style.textShadow="0 0 2px rgb(0 0 0)"
  document.getElementById("iconifyNotification").style.textShadow="0 0 2px rgb(0 0 0)"
  document.getElementById("iconifyMessage").style.textShadow="0 0 2px rgb(0 0 0)"
  document.getElementById("iconifyLogOut").style.textShadow="0 0 2px rgb(0 0 0)"
}

// tooltip
var mediaQuery = window.matchMedia('(min-width: 991.49px)')
if (mediaQuery.matches) {
  (function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()
}