/**
 * Created by svchost on 07.03.2016.
 */


$(document).ready(function() {
    $('.tr-clickable').click(function() {
        var href = $(this).find("a").attr("href");
        if (href) {
            window.location = href;
        }
    });
});