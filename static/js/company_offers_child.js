/**
 * Created by svchost on 13.03.2016.
 */



function acceptOffer(id, accept) {
    var answer = $('#textarea_' + id).val();
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
            alert('Could not accept offer!')
        }
    });

    return false;
}