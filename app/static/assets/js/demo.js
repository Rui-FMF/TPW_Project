$(document).ready(function () {
    $('.nk-product-rating, .nk-review-rating').each(function() {
        let rate = $(this).attr('data-rating');
        for (let i = 1; i <= 5; i++) {
            if (rate < i - 0.5)
                $(this).append('<i class="far fa-star"></i>');
            else if (rate >= i)
                $(this).append('<i class="fa fa-star"></i>');
            else
                $(this).append('<i class="fas fa-star-half"></i>');
        }
    });

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