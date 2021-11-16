$('body').on('click', '.authorization__data-password-view', function () {
    if ($('.authorization__data-password-input').attr('type') == 'password') {
        $(this).addClass('authorization__data-password-view-hidden');
        $('.authorization__data-password-input').attr('type', 'text');
    } else {
        $(this).removeClass('authorization__data-password-view-hidden');
        $('.authorization__data-password-input').attr('type', 'password');
    }
    return false;
});

