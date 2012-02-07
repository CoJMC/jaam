var app = {};
window.app = app;

app.models = {};
app.views = {};
app.collections = {};

app.models.BaseModel = Backbone.Model.extend({
	
});

app.collections.BaseList = Backbone.Collection.extend({
	
});

app.views.BaseView = Backbone.View.extend({
	/*
	render: function() {
		context = {data: this.model.toJSON() };
		elem = $(this.el);

		this.template(context, function(err, out) {
			elem.html(out);
		});
	}
	*/
});

$(document).ready(function() {
	var Router = Backbone.Router.extend({
		routes: {
			"": "index",
			"project/:projectid": "project",
			"project/:projectid/photos": "projectphotos",
			"project/:projectid/videos": "projectvideos",
		},
		index: function() {
			var projectList = new app.collections.ProjectList();
			var indexView = new app.views.IndexView({ model: projectList });
			projectList.fetch();
		},
		project: function(projectid) {
			alert();
			$("#content").html("");
		},
		projectphotos: function() {
			
		},
		projectvideos: function() {
			
		},
	});

	app.router = new Router;

	var r = Backbone.history.start({ pushState: true, root: '/roy/' });
	console.log(r);

	// https://github.com/tbranyen/backbone-boilerplate/blob/master/app/index.js
	$(document).on("click", "a:not([data-bypass])", function(evt) {
		var href = $(this).attr("href");
		var protocol = this.protocol + "//";
		
		if (href && href.slice(0, protocol.length) !== protocol) {
			evt.preventDefault();
			app.router.navigate(href, true);
		}
	});
});