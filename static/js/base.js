$(document).ready(function () {
    alert_message_fade()
});

function alert_message_fade(){
    $(".alert").fadeTo(5000, 500).slideUp(500, function(){
        $(".alert").slideUp(5000);
    });
}
