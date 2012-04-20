$(document).ready(function() {
        $("#fancybox-outer").css("background", "#262626");
        $("#login-link").fancybox({
            /*
            'padding'   : 2, 
            'width'     : 250,
            'height'    : 200,
            'autoDimensions'    : false,
            */
        });
        $("#share-link").fancybox({
            /*
            'padding'   : 2,
            'scrolling' : false,
            'width'     : 150,
            'height'    : 100,
            'autoDimensions'    : false,
            */
        });
        $("#openid-login").fancybox();
});