/* Project specific Javascript goes here. */
$(window).on('load', function () {
    console.log("HELLO");
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
        success: function () {
            console.log('success');
        },
        error: function (data) {
            console.log('error');
            console.log(data);
        }
    })
})