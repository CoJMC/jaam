var fix_apple_nonsense;
if(!fix_apple_nonsense) {
	fix_apple_nonsense = true
	$(document).ready(function() {
		$("a[class!=noeffect]").click(function() {
			window.location = this.getAttribute("href");
			return false;
		});

		// hide something? I don't know if we want this
		window.scrollTo(0,0.9);
	});
}