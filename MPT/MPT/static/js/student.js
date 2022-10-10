// ---------- Adding Datatables ------------------
$(document).ready( () => {
    $('#student-mark-table').DataTable({
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
  
$(document).ready( () => {
    $('#student-previous-table').DataTable({
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
$(document).ready( () =>  {
    $('#student-upcoming-table').DataTable({
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