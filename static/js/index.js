function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

function submit() {
    var text = $('#inp_text').val();
    if (text !== '') {
        $('#inp_text').val('');
        var div = $('div.d-flex.justify-content-end.mb-4').clone();
        div.find('.msg_cotainer_send').text(text);
        div.show();
        $('div.card-body.msg_card_body').append(div.get(0));
        $('div.card-body.msg_card_body').animate({
        scrollTop: $('div.card-body.msg_card_body').height()
      }, 800);
        getChatResponse(text);
    }
}

function getChatResponse(text) {
    var div = $('div.d-flex.justify-content-start.mb-4').clone();
    $.ajax({
        headers: {"X-CSRFToken": getCookie('csrftoken')},
        url: '/chat',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({'text': text}),
        success: function (data) {
            div.find('.msg_cotainer').text(data.text);
            div.show();
            $('div.card-body.msg_card_body').append(div.get(0));
            // $('div.card-body.msg_card_body').scrollTop($('div.card-body.msg_card_body').height());
            $('div.card-body.msg_card_body').animate({
        scrollTop: $('div.card-body.msg_card_body').height()
      }, 800);
        },
    });
}

$('div.card-body.msg_card_body').animate({
        scrollTop: $('div.card-body.msg_card_body').height()
      }, 800);

$(document).ready(function () {
    $.get('clear_session', function (data) {
        console.log("session cleared", data);
    })
});
