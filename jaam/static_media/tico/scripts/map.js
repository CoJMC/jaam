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
	
	//Messing with info 	
		
	var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
	
	var contentString = '<div id="content">'+
    '<div id="siteNotice">'+
    '</div>'+
    '<h2 id="firstHeading" class="firstHeading">Uluru</h2>'+
    '<div id="bodyContent">'+
    '</div>'+
    '</div>';

	var infowindow = new google.maps.InfoWindow({
	    content: contentString
	});
	
	var marker = new google.maps.Marker({
	    position: myLatlng,
	    map: map,
	    title:"Uluru (Ayers Rock)"
	});
	google.maps.event.addListener(marker, 'click', function() {
  	infowindow.open(map,marker);
	});
	
	function processChange() {
		if (JSONrequest.readyState == 4) {
			if (JSONrequest.status ==200){
				alert("Things are looking good!");
				jsonObject = JSON.parse(this.responseText);
				$("project_sidebar").children[0].style.color="green"
				var item = jsonObject.objects[0];
			}
			else {
				alert("There was a problem with returned data");
			}
		}
	}
	
	var JSONrequest = new XMLHttpRequest();
	JSONrequest.onreadystatechange = processChange();
	JSONrequest.open("GET", "http://dev.jaam.us.to:8000/api/v1/project/?format=json", true);
	JSONrequest.send(null);
	
}


