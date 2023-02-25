/* form_control.js */
$('.needs-validation').each(function () {
    var form = $(this);
    form.submit(function (event) {
        if (!form[0].checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.addClass('was-validated');
    });
});