var context = 0;

function submit() {
    var text = $('#inp_text').val();
    var div = $('div.d-flex.justify-content-end.mb-4').clone();
    div.find('.msg_cotainer_send').text(text);
    $('div.card-body.msg_card_body').append(div.get(0));
    if(context === 0){
        getChatResponse(text)
    }
}

function getChatResponse(text) {
    var div = $('div.d-flex.justify-content-start.mb-4').clone();
    $.get('/chat', {'text': text}, function (data) {
        div.find('.msg_cotainer').text(data.text);
        $('div.card-body.msg_card_body').append(div.get(0));
    })
}