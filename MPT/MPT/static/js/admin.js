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
$(document).ready( function () {
    $('#user-table').DataTable({
        //options
    });
} );
$(document).ready( function () {
    $('#student-table').DataTable({
        //options
    });
} );
$(document).ready( function () {
    $('#mentor-table').DataTable({
        //options
    });
} );
$(document).ready( function () {
    $('#activity-table').DataTable({
        //options
    });
} );