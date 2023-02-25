$(document).ready(function () {
    $('#resources').DataTable( {
        paging: false,
        scrollY: 400,
        scrollX: true,
        scrollCollapse: true,
        responsive: true,
        dom: 'frtipB',
            buttons: [
                { extend: 'excel', text: 'Export to Excel' }, 'print'
            ]
    });
});