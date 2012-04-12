var mouse_is_inside = false;
 
$(document).ready(function() {
    $(".share_btn").click(function() {
        var shareBox = $("#login_box");
        if (shareBox.is(":visible"))
            shareBox.fadeOut("fast");
        else
            shareBox.fadeIn("fast");
        return false;
    });
 
    $("#share_box").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });
 
    $("body").click(function(){
        if(! mouse_is_inside) $("#share_box").fadeOut("fast");
    });
});