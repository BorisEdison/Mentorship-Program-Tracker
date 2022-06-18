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
    // options
});
let mntr_table = new DataTable('#mentor-table', {
    // options
});
let actvt_table = new DataTable('#activity-table', {
    // options
});