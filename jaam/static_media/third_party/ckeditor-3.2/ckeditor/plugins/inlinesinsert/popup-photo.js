$(document).ready(function() {
  app = {
    models: {},
    views: {},
    collections: {},
    instances: {
      collections: {},
      models: {},
      views: {}
    },
    utils: {}
  };

  app.utils.selectTemplate = _.template($("#select-template").html());

  app.models.Project = Backbone.Model.extend({});
  app.models.PhotoGallery = Backbone.Model.extend({});

  app.collections.Projects = Backbone.Collection.extend({
    model: app.models.Project,
    url: '/api/v1/project',
    parse: function(response) {
      return response.objects;
    }
  });

  app.collections.PhotoGallerys = Backbone.Collection.extend({
    model: app.models.PhotoGallery,
    url: '/api/v1/photogallery',
    parse: function(response) {
      return response.objects;
    }
  });

  app.collections.ProjectList = Backbone.Collection.extend({ model: app.models.Project })

  app.models.Photo = Backbone.Model.extend({
    defaults: function () {
      return {
        image: 'https://www.google.com/logos/classicplus.png',
        id: "-1"
      };
    }
  });

  app.collections.Photos = Backbone.Collection.extend({
    model: app.models.Photo,
    url: '/api/v1/photo',
    parse: function(response) {
      return response.objects;
    }
  });

  app.views.PhotoView = Backbone.View.extend({
    tagName: "li",
    template: _.template($("#photo-template").html()),
    events: {
      "click a": "insertImage",
    },
    insertImage: function(e) {
      var htmlToInsert = "{{ photo {id} }}";
      htmlToInsert = htmlToInsert.replace("{src}", this.model.attributes.image);
      htmlToInsert = htmlToInsert.replace("{id}", this.model.attributes.id);
      //htmlToInsert = htmlToInsert.replace("{args}", this.model.attributes.i);
      if(window.opener == null) {
        alert("You MUST use this from the popup window");
        return;
      }
      window.opener.ckeditor_inlinesinsert.insertHtml(htmlToInsert);
    },
    render: function() {
      $(this.el).html(this.template({
        url: this.model.attributes.image,
        id: this.model.attributes.id
      })).addClass("span2");
      return this;
    },
  });

  app.views.AppView = Backbone.View.extend({
    el: "#photoSelector",
    events: {
      "change #projectSelector": "changeProject",
      "change #gallerySelector": "changeGallery",
    },
    initialize: function() {
      app.instances.collections.projects = new app.collections.Projects;
      app.instances.collections.photogallerys = new app.collections.PhotoGallerys;
      app.instances.collections.photos = new app.collections.Photos;

      app.instances.collections.photos.bind('add', this.addOne, this);
      app.instances.collections.photos.bind('reset', this.addAll, this);

      app.instances.collections.projects.bind('add', this.renderP, this);
      app.instances.collections.projects.bind('reset', this.renderP, this);

      app.instances.collections.photogallerys.bind('add', this.renderPG, this);
      app.instances.collections.photogallerys.bind('reset', this.renderPG, this);
      
      app.instances.collections.photos.url = "/api/v1/photo/?size=200,200";
      app.instances.collections.projects.fetch();
      app.instances.collections.photogallerys.fetch();
      app.instances.collections.photos.fetch();
    },
    addOne: function(photo) {
      var view = new app.views.PhotoView({model: photo});
      $("#photoList").append(view.render().el);
    },
    addAll: function(photos) {
      //console.log("reset");
      //console.log(app.instances.collections.photos);
      //console.log("/reset");
      $("#photoList").html("");
      photos.each(this.addOne);
    },
    renderPG: function(e) {
      // modify gallery select
      var galleryOptions = {};
      _.each(app.instances.collections.photogallerys.models, function(gallery, i) {
        galleryOptions[i] = {
          id: gallery.attributes.id,
          value: gallery.attributes.title
        }
      });
      $("#gallerySelectorContainer").html(app.utils.selectTemplate({ id: 'gallerySelector', options: galleryOptions, label: 'Gallery:' }));
      // end gallery select
    },
    renderP: function() {
      // initial load for the projects
      var projectOptions = {};
      _.each(app.instances.collections.projects.models, function(project, i) {
        projectOptions[i] = {
          id: project.attributes.id,
          value: project.attributes.title
        }
      });
      $("#projectSelectorContainer").html(app.utils.selectTemplate({ id: 'projectSelector', options: projectOptions, label: 'Project:' }));
      // end initial project load
      return this.el;
    },
    changeProject: function(e) {
      // update url for galleries
      // update select box
      $("#gallerySelector").val("null");
      app.instances.collections.photogallerys.url = "/api/v1/photogallery/";
      var project_id = $("#projectSelector").val();
      if(project_id != "null") {
        app.instances.collections.photogallerys.url += "?project__id=" + project_id;
      }
      app.instances.collections.photogallerys.reset();
      app.instances.collections.photogallerys.fetch();
      this.changeGallery();
    },
    changeGallery: function(e) {
      app.instances.collections.photos.url = "/api/v1/photo/";
      var gallery_id = $("#gallerySelector").val();
      var project_id = $("#projectSelector").val();
      //console.log(project_id);
      //console.log(gallery_id);
      if(gallery_id != "null") {
        app.instances.collections.photos.url += "?gallery__id=" + gallery_id + "&size=200,200"
      } else if(project_id != "null") {
        app.instances.collections.photos.url += "?project__id=" + project_id + "&size=200,200";
      } else {
        app.instances.collections.photos.url += "?size=200,200";
      }
      console.log(app.instances.collections.photos.url)
      app.instances.collections.photos.reset();
      app.instances.collections.photos.fetch();
    },
  });

  app.instances.views.appview = new app.views.AppView();
});