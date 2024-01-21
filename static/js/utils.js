function showSnackbar(msg_class, msg) {
    $('#snackbar').addClass(`show-bar ${msg_class}`);
    $('#snackbar').html(msg);
    setTimeout(function () {
        $('#snackbar').removeClass('show-bar');
        $('#snackbar').removeClass(msg_class);
        $('#snackbar').html('');
    }, 3000);
}



/*
* @Param {String} message
* @Param {Element} element
* @Param {Boolean} enabled
*/
function displayLoadingText(element, message, enabled) {
    element.html(message)
    element.prop("disabled", enabled)
}
