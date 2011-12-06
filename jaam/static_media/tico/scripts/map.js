function initialize() {
    var latlng = new google.maps.LatLng(0, 0);
    var styleArray = [
    	{
    		featureType: "administrative",
    		elementType:"labels",
    		stylers: [
      			{ visibility: "off" }
    		]
  		},{
		    featureType: "administrative.province",
		    stylers: [
		      { visibility: "off" }
		    ]
		},{
		    featureType: "poi",
		    stylers: [
		      { visibility: "off" }
		    ]
		},{
    		featureType: "road",
    		stylers: [
    			{ saturation: -100 }
    		]
    	},{
		    featureType: "water",
		    elementType: "labels",
		    stylers: [
		      { visibility: "off" }
		    ]
  		} ];
    var myOptions = {
      zoom: 2,
      minZoom: 2,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      styles: styleArray
    };    
    var map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
    var marker = new google.maps.Marker({
	  position: new google.maps.LatLng(56.8848, 14.7730),
	  map: map
	});
	var marker = new google.maps.Marker({
	  position: new google.maps.LatLng(40.815, -96.705),
	  map: map
	});
}
