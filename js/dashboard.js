// sidebar
(function () {
    'use strict'
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()

// kebab menu
var kebab = document.querySelector('.kebab'),
middle = document.querySelector('.kebab-middle'),
cross = document.querySelector('.kebab-cross'),
dropdown = document.querySelector('.kebab-dropdown');

kebab.addEventListener('click', function() {
middle.classList.toggle('active');
cross.classList.toggle('active');
dropdown.classList.toggle('active');
})