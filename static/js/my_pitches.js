/**
 * Created by skDn on 11/03/2016.
 */

var $myPitchesTable = $('#myPitches');

var $tableRecords = $myPitchesTable.find('tbody').children('tr');

$(function () {
    var updateProgress = function () {
        $tableRecords.each(function () {
            var progressDiv = $(this).find('.progress');

            var progress = $(this).data().progress;
            var height = $(this).height();

            progressDiv.css('left', progress - 100 + '%');
            progressDiv.css('height', height + 'px');

            progressDiv.css('top', $(this).position().top + 1 + 'px');
        });
    };

    updateProgress();
});
