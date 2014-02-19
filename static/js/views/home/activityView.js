define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/home/activityTemplate.html',
  
 
], function($, _, Backbone,Mustache,pTemplate ){



		 var activityView = Backbone.View.extend({ 
		 	tagName: "div",
		 
		    initialize: function(){
		    	
		      _.bindAll(this, 'render');
		    },
		    render: function(){
		    		$(this.el).html (  Mustache.to_html( pTemplate , this.model.toJSON())  );
		    
		    	return this;
		    }


		 });


		 return activityView;
});

