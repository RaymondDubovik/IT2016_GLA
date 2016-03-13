/**
 * Created by svchost on 13.03.2016.
 */

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