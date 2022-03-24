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