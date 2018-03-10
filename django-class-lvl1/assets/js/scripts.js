/* Project specific Javascript goes here. */

/* Add todo_item by submit form */
$(document).on('submit', '#inputTodo', function (e) {
    e.preventDefault();
    var todoValue = $('#addTodo').val();
    $('#addTodo').val('');

    $.ajax({
        method: 'POST',
        url: '/ajax/add/',
        // data: $(this).serialize(),
        data: {
            text: todoValue,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            console.log('success');
            $('#listTodo').prepend(
                '<a href="#" data-id="' + data.todo.id + '" class="list-group-item list-group-item-action">\n' +
                '   <span>' + data.todo.text + '</span>\n' +
                '</a>'
            )
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
});

/* Change status of todo_item */
$('#listTodo').on('click', '.list-group-item', function (e) {
    e.preventDefault();

    if (!$(this).hasClass('disabled')) {
        $(this).addClass('disabled');
    } else {
        $(this).removeClass('disabled');
    }

    $.ajax({
        method: 'POST',
        url: '/ajax/status/',
        data: {
            id: $(this).data('id'),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            console.log('success');
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
});

/* Deleting completed todo_items */
$('#delButtons').on('click', '#delCompleted', function (e) {
    e.preventDefault();
    var idList = [];

    $('.disabled').each(function () {
        idList.push($(this).data('id'));
        $(this).remove();
    });

    console.log(idList);

    $.ajax({
        method: 'POST',
        url: '/ajax/delete-completed/',
        data: {
            id_list: JSON.stringify(idList),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            console.log('success');
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
});

/* Deleting all todo_items */
$('#delButtons').on('click', '#delAll', function (e) {
    e.preventDefault();

    $('.list-group-item').each(function () {
        $(this).remove();
    });

    $.ajax({
        method: 'POST',
        url: '/ajax/delete-all/',
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            console.log('success');
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
});
