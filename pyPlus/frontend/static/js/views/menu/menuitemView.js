define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/menu/itemTemplate.html',



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

				
		    },
		    


		 });


		 return activityView;
});

