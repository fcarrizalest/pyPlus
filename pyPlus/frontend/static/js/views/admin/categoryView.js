define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/admin/categoryTemplate.html',



], function($, _, Backbone,Mustache,pTemplate ){



		 var activityView = Backbone.View.extend({
		 	tagName: "li",

		    initialize: function(){

		      _.bindAll(this, 'render');
		    },
		    render: function(){


		    		$(this.el).html (  Mustache.to_html( pTemplate , this.model.toJSON())  );


		    	return this;
		    },events:{

				"click .editC":"editButton",
				"click .deleteC": "deleteButton"
		    },
		    deleteButton:function(){

				var t = this.model;
		    	this.model.destroy( {wait: true , success: function(model, response) {
						console.log(t.parent)
				}});



		    },
		    editButton:function(){


				this.model.set( "name" ,  $(this.el).find("input")[0].value);
				var csrf_token = $('meta[name=csrf_token]').attr("content");

				this.model.set( "csrf_token" , csrf_token);
				this.model.save();
		    }


		 });


		 return activityView;
});

