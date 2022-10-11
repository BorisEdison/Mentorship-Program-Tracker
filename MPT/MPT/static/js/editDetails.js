//  ------------------- Edit profile in student dash Scrollspy---------------------- //
let editLink = document.getElementsByName("edit-link");
let editBody = document.getElementsByName("edit-body");
let options = {
  threshold: 0.6,
};
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) {
      return;
    }
    editLink.forEach((e) => {
      e.classList.add("active");
      if (e.getAttribute("href") != "#" + entry.target.id) {
        e.classList.remove("active");
      }
    });
  });
}, options);
editBody.forEach((elem) => {
  observer.observe(elem);
});

// -----------Image File Size ---------------------
function validateSize(input) {
    const fileSize = input.files[0].size / 1024; // in KiB
  // console.log(fileSize)
    if (fileSize > 500) {
        alert('File size exceeds 500 KiB');
        input.value = '';
        return;
    }

}

// ---------- Adding Datatables ------------------
$(document).ready( function () {
  $('#marks-table').DataTable({
      //options
      dom: 'Blfrtip',
      select:true,
      "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
      dom: 'Bfrtip',
      buttons: [
      'copyHtml5',
      'excelHtml5',
      'csvHtml5',
      'pdfHtml5',
      'print',
      'pageLength',
      ]
});
} );