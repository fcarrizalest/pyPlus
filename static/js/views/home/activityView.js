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
		    		

		    		$(this.el).addClass("activityRow");

		    		console.log("Render activityView ");
		    		console.log(this.model);

		    		this.model.fetch();
		    			


		    	return this;
		    }


		 });


		 return activityView;
});

