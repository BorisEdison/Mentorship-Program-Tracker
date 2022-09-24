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
// $(document).ready( function () {
//     $('#user-table').DataTable({
//         //options
//     });
// } );

$(document).ready(function() {
    $('#user-table').DataTable( {
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
    } );
} );

$(document).ready( function () {
    $('#student-table').DataTable({
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

$(document).ready( function () {
    $('#mentor-table').DataTable({
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

$(document).ready( function () {
    $('#activity-table').DataTable({
        //options

    });
} );

$(document).ready( function () {
    $('#announcement-table').DataTable({
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
$(document).ready( function () {
    $('#previous-table').DataTable({
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
  $(document).ready( function () {
    $('#upcoming-table').DataTable({
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