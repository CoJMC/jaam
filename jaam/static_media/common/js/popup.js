function toggle(div_id) {
	var el = document.getElementById(div_id);
	if ( el.style.display == 'none' ) {	el.style.display = 'block';}
	else {el.style.display = 'none';}
}
function blanket_size(popUpDivVar) {
	if (typeof window.innerWidth != 'undefined') {
		viewportheight = window.innerHeight;
	} else {
		viewportheight = document.documentElement.clientHeight;
	}
	if ((viewportheight > document.body.parentNode.scrollHeight) && (viewportheight > document.body.parentNode.clientHeight)) {
		blanket_height = viewportheight;
	} else {
		if (document.body.parentNode.clientHeight > document.body.parentNode.scrollHeight) {
			blanket_height = document.body.parentNode.clientHeight;
		} else {
			blanket_height = document.body.parentNode.scrollHeight;
		}
	}
	var blanket = document.getElementById('blanket');
	blanket.style.height = blanket_height + 'px';

}

function popup(windowname) {
	blanket_size(windowname);
	toggle('blanket');
	toggle(windowname);		
}

function determinePage(pathname) {
	
	if (pathname.search("info") != -1) {
		popOutLink('blip_info', 'link_info');}
		
	else if (pathname.search("photos") != -1) {
		popOutLink('blip_photo', 'link_photo');}
		
	else if (pathname.search("video") != -1) {
		popOutLink('blip_video', 'link_video');}
			
	else if (pathname.search("stories") != -1) {
		popOutLink('blip_story', 'link_story');}
					
	else if (pathname.search("blog") != -1) {
		popOutLink('blip_blog', 'link_blog');}
			
	else if (pathname.search("contributor") != -1) {
		popOutLink('blip_contributor', 'link_contributor');}		
	}
	
function popOutLink(blip, link) {
		document.getElementById(blip).style.visibility="visible";
		document.getElementById(link).style.marginLeft="-20px"; 	
}
