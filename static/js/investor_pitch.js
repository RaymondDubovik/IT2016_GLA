/**
 * Created by svchost on 13.03.2016.
 */

$( document ).ready(function() {
    var $offerSubmit = $('#offerSubmit');
    var $stocksOffer = $('#stocks_offer');
    var $stocksPrice = $('#stocks_price');
    var $stocksMessage = $('#stocks_message');
    var $offers = $('#offers');
    var $yourOffers = $('#your_offers');
    var $yourOffersSuccess = $('#your_offers_success');

    $offerSubmit.click(function (e) {
        var stockCount = $stocksOffer.val();
        var stockPrice = $stocksPrice.val();
        var stockOfferMessage = $stocksMessage.val();

        if (!stockCount) {
            $stocksOffer.focus();
            alert('empty offer');
            return;
        }

        if (!stockPrice) {
            $stocksPrice.focus();
            alert('empty price');
            return;
        }

        if (!stockOfferMessage) {
            $stocksMessage.focus();
            alert('empty message');
            return;
        }

        $.get('/pitchify/investor/add_offer/' + pitchId + '/' + stockCount + '/' + stockPrice + '/' + stockOfferMessage + '/' , function(json) {
            if (json['success']) {
                var id = json.id;
                $stocksOffer.val('');
                $stocksPrice.val('');
                $stocksMessage.val('');

                $yourOffers.hide(300);
                $yourOffersSuccess.show(300);

                $offers.prepend(
                    '<div id="offer_' + id + '" class="alert alert-info">'+
                        '<div class="text-left">'+
                            '<div class="full-width">'+
                                '<p>'+
                                    '<span> ' + stockCount + ' stocks for ' + stockPrice + '£</span>'+
                                    '<span class="float-right">Pending<a href="#" onClick="removeOffer(' + id + ')">(Delete)</a></span>'+
                                '</p>'+
                            '</div>'+
                            '<p>' + stockOfferMessage + '</p>'+
                        '</div>'+
                    '</div>'
                );
           } else {
                alert('Could not add offer: ' + json.error)
           }
        });
    })
});


function removeOffer(id) {
    BootstrapDialog.show({
        message: 'Warning! This action is not reversible. Do you really want to delete this Offer?',
        buttons: [{
            icon: 'glyphicon glyphicon-trash',
            label: 'Delete',
            cssClass: 'btn-danger',
            action: function (thisDialog) {
                $.get('/pitchify/investor/remove_offer/' + id, function(json) {
                   console.log(json);
                    if (json['success']) {
                       $('#offer_' + id).hide(300);
                   } else {
                        alert('Could not delete offer!')
                   }
                });

                thisDialog.close();
            }
        }, {
            label: 'Cancel',
            action: function (thisDialog) {
                thisDialog.close();
            }
        }]
    });

    return false;
}