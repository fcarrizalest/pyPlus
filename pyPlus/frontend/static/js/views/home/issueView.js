define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  



], function($, _, Backbone,Mustache ){



		 var activityView = Backbone.View.extend({
		 	tagName: "option",

		    initialize: function(){

		      _.bindAll(this, 'render');
		    },
		    render: function(){


		    	$(this.el).html (  this.model.get("name")  );
	    		
	    		$(this.el).attr("value", this.model.get("id"));

		    	return this;
		    },events:{

				
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

