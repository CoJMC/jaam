app.views.IndexView = app.views.BaseView.extend({
	el: '#content',
	template: dust.compileFn($('#coverphoto-template').html()),
	initialize: function() {
		this.model.bind('reset', this.addProjects, this);
	},
	addProject: function(project) {
		var photoCover = new app.collections.PhotoList();
		photoCover.url = '/api/v1/photo/?project__id=' + project.toJSON().id;
		photoCover.bind('reset', this.renderCoverphoto(project), this);
		photoCover.fetch();
	},
	addProjects: function(projects) {
		$(this.el).html();
		projects.each(this.addProject, this);
	},
	renderCoverphoto: function(project) {
		var element = this.el;
		return function(photos) {
			var context = { "project": project.toJSON(), "photos": photos.toJSON() };
			
			this.template(context, function(err, out) {
				$(element).append(out);
			});
		}
	}
});