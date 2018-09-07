var frm = $('#new_note');
frm.submit(function () {
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function (data) {
            //$('#test').html(data)); ответ - вся страница
        }
    });
    return false;
});
