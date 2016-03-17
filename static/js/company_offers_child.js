/**
 * Created by svchost on 13.03.2016.
 */

var $edit = $('#edit');
var $editSuccess = $('#edit-success');
var $editYoutube = $('#edit-youtube');
var $editDescription = $('#edit-description');
var $youtubeIframe = $('#youtube-iframe');
var $description = $('#description');

$('#edit-btn').click(function (e) {
    $edit.toggle(300);
});

function editPitch(id) {
    var youtube = $editYoutube.val();
    var description = $editDescription.val();

    var url = '/pitchify/company/edit_pitch/' + id + '/' + encodeURIComponent(youtube) + '/' + encodeURIComponent(description) + '/';
    $.get(url, function (json) {
        if (json['success']) {
            if (json['youtubeId']) {
                var youtubeUrl = 'https://www.youtube.com/embed/' + json['youtubeId'];
                $youtubeIframe.attr('src', youtubeUrl);
            }

            $description.html(description);
            $edit.hide(300);
            $editSuccess.show(300);
        } else {
            alert('no success');
        }
    });
}

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

    var url = '/pitchify/company/accept_offer/' + id + '/' + accept + '/' + answer + '/';
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

            console.log(json);

            var soldStocks = json['soldStocks'];
            var percentage = Math.round(soldStocks * 100.0 / json['totalStocks']);

            $('#stocks-sold').html(soldStocks);
            $progressbar = $('#progressbar-claimed');

            console.log(percentage);

            $progressbar.width(percentage * 4);
            $progressbar.html(percentage);
            $('#invested').html(json['invested']);
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