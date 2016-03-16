/**
 * Created by svchost on 13.03.2016.
 */



function acceptOffer(id, accept) {
    var $textarea = $('#textarea_' + id);
    var answer = $textarea.val();

    if (answer.length <= 0) {
        BootstrapDialog.show({
            message: "Please, fill in the answer!",
            buttons: [{
                cssClass: 'btn-danger',
                label: 'OK',
                action: function (thisDialog) {
                    thisDialog.close();
                    $textarea.focus();
                }
            }]
        });


        return;
    }

    var url = '/pitchify/company/accept_offer/' + id +'/' + accept + '/' + answer + '/';
    var $offer = $('#offer_' + id);

    $.get(url, function (json) {
        if (json['success']) {
            $offer.toggleClass('alert-info');

            if (accept) {
                $offer.addClass('alert-success');
            } else {
                $offer.addClass('alert-danger');
            }

            var $answer = $('#answer_' + id);

            $answer.empty().append(
                $('<p />').html('Answer: ' + answer)
            );

            $('#buttons_' + id).empty();
        } else {
            BootstrapDialog.show({
                message: json['message'],
                buttons: [{
                    cssClass: 'btn-danger',
                    label: 'OK',
                    action: function (thisDialog) {
                        thisDialog.close();
                    }
                }]
            });
        }
    });

    return false;
}