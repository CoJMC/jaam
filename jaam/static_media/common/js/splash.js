function runSplash() {
    var lastDate=getCookie("GlobalEyewitness");
    if (lastDate==null || lastDate=="") {

        $("#footer").hide();
        $("#container").hide();
        
        $("#JaamIntro").show();

        var lastDate = "JournalismMeans";
        setCookie("GlobalEyewitness",lastDate,null);
        
        $("#JaamIntro").delay(1000).fadeOut("slow");
        $("#container").delay(1200).fadeIn("slow");
        $("#footer").delay(1400).fadeIn("slow");
    }
}

function setCookie(c_name,value,exdays)
{
    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
}

function getCookie(c_name) {
    var i, x, y
    var ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++) {
        x = ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x = x.replace(/^\s+|\s+$/g,"");
        if (x==c_name) {
            return unescape(y);
        }
    }
}