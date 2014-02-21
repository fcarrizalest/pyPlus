define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/home/commentTemplate.html',

  
 
], function($, _, Backbone,Mustache,commentTemplate  ){



	var commentView = Backbone.View.extend({ 
		 	tagName: "div",
		 
		    initialize: function(){
		    	
		      _.bindAll(this, 'render');
		    },
		    render: function(){ 

		    	$(this.el).html (  Mustache.to_html( commentTemplate , this.model.toJSON())  );
		    		
		    	
		    	$(this.el).addClass("commentRow");

		    	$(this.el).append( this.model.get("object").content );

		    	return this;

		    },
		});

	return commentView;


} );
