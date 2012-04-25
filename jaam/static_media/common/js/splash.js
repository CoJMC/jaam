function runSplash() {
    var SPLASH_RUNTIME = 3000;
    var FOOTER_TIMEOFFSET = 500;
    var DEMO_MODE = true;
    
    var lastDate=getCookie("GlobalEyewitness");
    var defer = $.Deferred();

    if (lastDate==null || lastDate=="" || DEMO_MODE) {
        $("#footer").hide();
        $("#JaamIntro").show();

        var lastDate = "JournalismMeans";
        setCookie("GlobalEyewitness",lastDate,null);
        
        $("#JaamIntro").delay(SPLASH_RUNTIME).fadeOut("slow", function() {
            defer.resolve();
        });

        $("#footer").delay(SPLASH_RUNTIME+FOOTER_TIMEOFFSET).fadeIn("slow");
    } else {
        defer.resolve();
    }

    return defer;
}

function setCookie(c_name,value,exdays) {
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