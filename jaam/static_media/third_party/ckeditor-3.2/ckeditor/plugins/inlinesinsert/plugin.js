CKEDITOR.plugins.add('inlinesinsert',
{
	init: function( editor )
	{
		editor.addCommand('inlinesinsert-photo', {
			exec: function(editor) {
				window.ckeditor_inlinesinsert = editor;
				newwindow = window.open(CKEDITOR.plugins.getPath('inlinesinsert') + 'popup-photo.html',
								'inlinesinsert_popup', 'height=350,width=700');
				if (window.focus) {
					newwindow.focus()
				}
			}
		})

		editor.addCommand('inlinesinsert-video', {
			exec: function(editor) {
				window.ckeditor_inlinesinsert = editor;
				newwindow = window.open(CKEDITOR.plugins.getPath('inlinesinsert') + 'popup-video.html',
								'inlinesinsert_popup', 'height=350,width=700');
				if (window.focus) {
					newwindow.focus()
				}
			}
		})

		editor.ui.addButton('inlinesinsert-photo', {
			label: 'Insert Photo',
			command: 'inlinesinsert-photo',
			className: 'cke_button_image'
			
			/* The className property handles the button icon. There was a thread on StackOverflow
				that mentions doing it the below way if we want to use a custom icon, but I couldn't
				get it to work.
				
				icon: this.path + 'images/inlinesinsert-photo.png'
			*/

		})

		/*editor.ui.addButton('inlinesinsert-video', {
			label: 'Insert Video',
			command: 'inlinesinsert-video',
			icon: this.path + 'images/inlinesinsert-video.png'
		})*/
	}
} );