app.models.Project = app.models.BaseModel.extend({
	
});

app.collections.ProjectList = app.collections.BaseList.extend({
	model: app.models.Project,
	url: '/api/v1/project/',
	parse: function(data) {
		return data.objects;
	},
});