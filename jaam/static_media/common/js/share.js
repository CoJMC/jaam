//var mouse_is_inside = false;
 
$(document).ready(function() {
    var getUrl = function() {
        return window.location
    }
    var getTitle = function() {
        return document.title
    }
    $("#share-facebook-btn").click(function() {
        var link = "https://www.facebook.com/sharer.php?u=" + encodeURIComponent(getUrl()) + "&t=" + encodeURIComponent(getTitle());
        console.log("opening: " + link);
        window.open(link, "_blank");
    });
    $("#share-twitter-btn").click(function() {
        var link = "https://twitter.com/intent/tweet?url=" + encodeURIComponent(getUrl()) + "&text=" + encodeURIComponent(getTitle());
        console.log("opening: " + link);
        window.open(link, "_blank");
    });
    $("#share-pinterest-btn").click(function() {
        var link = "http://pinterest.com/pin/create/button/?url=" + encodeURIComponent(getUrl()) + "&text=" + encodeURIComponent(getTitle());
        console.log("opening: " + link);
        window.open(link, "_blank");
    });
});