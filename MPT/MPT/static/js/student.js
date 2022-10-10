// ---------- Adding Datatables ------------------
$(document).ready( function () {
    $('#student-marks-table').DataTable({
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
});