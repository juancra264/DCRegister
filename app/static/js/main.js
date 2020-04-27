$(document).ready(function () {
    $('#datatable').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'excel', 'pdf'
        ]
    });
});