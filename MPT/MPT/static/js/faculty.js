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
$(document).ready( function () {
  $('#sendTo-table').DataTable({
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