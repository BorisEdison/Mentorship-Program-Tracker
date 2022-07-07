// search
// $(document).ready(function(){
//     $("#myInput").on("keyup", function() {
//       var value = $(this).val().toLowerCase();
//       $("#myTable tr").filter(function() {
//         $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//       });
//     });
//   });



// ---------- Adding Datatables ------------------
let usr_table = new DataTable('#user-table', {
    // options
});
let studnt_table = new DataTable('#student-table', {

});

let mntr_table = new DataTable('#mentor-table', {
    // options
});
let actvt_table = new DataTable('#activity-table', {
    // options
});

// ----------------- Select button on Admin dash ------------------------ //
// let btns = document.getElementsByName("btn-show");
// let cbs = document.getElementsByName("cb-choose");
// let btn_assign = document.getElementById("assign-btn");
// let btn_cancel = document.getElementById("cancel-btn");

// const btn_status = (status) => {
//     btns.forEach((btn) => {

//     });
//     cbs.forEach((cb) => {
//         cb.style.opacity = status ? "0" : "1";
//     });
// };