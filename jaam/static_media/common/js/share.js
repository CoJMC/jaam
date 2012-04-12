var mouse_is_inside = false;
 
$(document).ready(function() {
    $(".share_btn").click(function() {
        var shareBox = $("#share_box_content");
        if (shareBox.is(":visible"))
            shareBox.fadeOut("fast");
          /*  $("#share_text").style.visibility="visible"; */
        else
            shareBox.fadeIn("fast");
           /*	 $("#share_text").style.visibility="hidden"; */
        return false;
    });
 
    $("#share_box_content").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });
 
    $("body").click(function(){
        if(! mouse_is_inside) $("#share_box_content").fadeOut("fast");
    });
});