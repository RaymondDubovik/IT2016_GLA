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
                BootstrapDialog.show({
                    message: 'Could not add offer: ' + json['message'],
                    buttons: [{
                        label: 'OK',
                        cssClass: 'btn-danger',
                        action: function (thisDialog) {
                            thisDialog.close();
                        }
                    }]
                });

           }
        });
    })
});