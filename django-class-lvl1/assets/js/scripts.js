/* Project specific Javascript goes here. */

$(window).on('load', function () {
    console.log("JS is CONNECTED");
})

$('#listTodo').on('click', '.list-group-item', function (e) {
    e.preventDefault();

    console.log('CATCH');

    if (!$(this).hasClass('disabled')) {
        $(this).addClass('disabled')
    }
})

$(document).on('submit', '#inputTodo', function (e) {
    e.preventDefault();
    console.log($('#addTodo').val());
    console.log($(this).serialize());

    $.ajax({
        method: 'POST',
        url: '/ajax/add/',
        // data: $(this).serialize(),
        data: {
            text: $('#addTodo').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            console.log('success');
            console.log(data);
            $('#listTodo').prepend(
                '<a href="#" id="todo' + data.todo.id + '" class="list-group-item list-group-item-action">\n' +
                '   <span>' + data.todo.text + '</span>\n' +
                '</a>'
            )
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
})


// $(document).on('click', '#listTodo .list-group-item', function (e) {
//     e.preventDefault();
//
//     if (!$(this).hasClass('disabled')) {
//         $(this).addClass('disabled')
//     }
// })