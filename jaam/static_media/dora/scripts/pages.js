function resizeImage()
{
	var window_height = document.body.clientHeight
	var window_width  = document.body.clientWidth
	var photo = document.getElementById("first_photo")
	var image_width   = photo.width
	var image_height  = photo.height
	var height_ratio  = image_height / window_height
	var width_ratio   = image_width / window_width
	if (height_ratio > width_ratio)
	{
		photo.style.width  = "auto"
		photo.style.height = "100%"
	}
	else
	{
		photo.style.width  = "100%"
		photo.style.height = "auto"
	}
}