
const input = document.getElementById('imgsize')
input.addEventListener('change', (event) => {
  const target = event.target
  	if (target.files && target.files[0]) {

      /*Maximum allowed size in bytes
        1MB Example
        Change first operand(multiplier) for your needs*/
      const maxAllowedSize = 1024 * 1024;
      if (target.files[0].size > maxAllowedSize) {
      	// Here you can ask your users to load correct file
       	target.value = ''
      }
  }
})