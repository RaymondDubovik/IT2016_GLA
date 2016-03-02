/**
 * Created by yordanyordanov on 02/03/2016.
 */

var userFormId = "#userForm";
var companyFormId = "#companyForm";
var investorFormId = "#investorForm";
var userTypeSelector = "#id_type";

$(companyFormId).hide();
$(investorFormId).hide();

$(userFormId).find('input').each(function(){
    $(this).addClass('form-control input-lg');
});



$(userTypeSelector).change(function() {
    if ($(this).val() === 'C') {
        $(investorFormId).hide();
        $(companyFormId).show();
    }
    if ($(this).val() === 'I') {
        $(companyFormId).hide();
        $(investorFormId).show();
    }
});
