$(document).ready(function () {
    if ($('#nk-nav-mobile').hasClass('open')) {
        let e = $('.demo-js').find('form').children('a');
        e.addClass('demo-opened');
        e.removeClass('demo-closed');
    }

    $('.single-icon').click(function() {
        let e = $('.demo-js').find('form').children('a');
        e.removeClass('demo-opened');
        e.addClass('demo-closed');
    });

    $('.demo-js').click(function() {
        let e = $(this).find('form').children('a');
        if ($('#nk-nav-mobile').hasClass('open')) {
            if ($(this).hasClass('open')) {
                e.removeClass('demo-opened');
                e.addClass('demo-closed');
            } else {
                e.addClass('demo-opened');
                e.removeClass('demo-closed');
            }
        } else {
            e.addClass('demo-opened');
            e.removeClass('demo-closed');
        }
    });
});