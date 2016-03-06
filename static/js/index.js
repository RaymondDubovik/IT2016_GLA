/**
 * Created by yordanyordanov on 02/03/2016.
 */
var $form = $("#user_form")
var $userFormId = $("#userForm");
var $companyFormId = $("#companyForm");
var $investorFormId = $("#investorForm");

var $userTypeSelector = $("#id_type");
var $companyDescription = $("#id_description");

// adding bootstrap classes to select and textarea elements
$companyDescription.addClass("form-control input-lg");
$companyDescription.attr("placeholder", "Please describe your company...");
$userTypeSelector.addClass("form-control input-lg");

// adding bootstrap class to form element.
$form.addClass("form");


$companyFormId.hide();
$investorFormId.hide();

$userTypeSelector.change(function() {
    if ($(this).val() === 'C') {
        $investorFormId.hide();
        $companyFormId.show();
    }
    if ($(this).val() === 'I') {
        $companyFormId.hide();
        $investorFormId.show();
    }
});
