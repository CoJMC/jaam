app.models.Photo = Backbone.Model.extend({
	
});

app.collections.PhotoList = Backbone.Collection.extend({
	model: app.models.Photo,
	url: '/api/v1/photo/',
	parse: function(data) {
		return data.objects;
	},
});