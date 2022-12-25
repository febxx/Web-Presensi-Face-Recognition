var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
var modal = $('#modal-system');

$(document).ready(function () {
    function getForm(event) {
        console.log('sadads')
        event.preventDefault();
        var btn = $(this);
        var url = btn.attr('href');
        var params = [];
        params['url'] = url;
        AjaxGETForm(params);
    }
    function delForm(event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.attr('href');
        var params = [];
        params['url'] = url+'delete';
        AjaxGETForm(params);
    }

    function delConfirm(event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.attr('href');
        var params = [];
        params['url'] = url+'delete/confirm';
        AjaxGETNotif(params);
    }

    function postForm(event) {
        event.preventDefault();
        var btn = $(this);
        var form = btn.closest('form');
        var url = form.attr('action');
        var params = [];
        params['url'] = url;
        params['method'] = form.attr('method');
        params['query'] = form.serialize();
        AjaxPOSTForm(params);
    }

    $('#kelasItems').on('click', '.get-form', getForm);
    $('#kelasItems').on('click', '.del-form', delForm);
    $('#shiftItems').on('click', '.get-form', getForm);
    $('#shiftItems').on('click', '.del-form', delForm);
    $('#pegawaiItems').on('click', '.get-form', getForm);
    $('#pegawaiItems').on('click', '.del-form', delForm);

    modal.on('click', '.save-form', postForm);
    modal.on('click', '.del-item', delConfirm);
});

function AjaxGETForm(params) {
    $.ajax({
        url: params['url'],
        type: 'GET',
        success: function (data) {
            modal.find('.modal-content').html(data.template);
            modal.modal();
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}


function AjaxPOSTForm(params) {
    $.ajax({
        url: params['url'],
        type: params['method'],
        data: params['query'],
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
        },
        success: function (data) {
            notification[data.valid](data.message);

            if (data.valid === 'success') {
                modal.modal('hide');

                setTimeout(function () {
                    location.reload();
                }, 2000);
            }
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}

function AjaxGETNotif(params) {
    $.ajax({
        url: params['url'],
        type: 'GET',
        success: function (data) {
            notification[data.valid](data.message);

            if (data.valid === 'success') {
                modal.modal('hide');
                setTimeout(function () {
                    location.reload();
                }, 2000);
            }
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}
