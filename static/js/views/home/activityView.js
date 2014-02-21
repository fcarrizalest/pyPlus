define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/home/activityTemplate.html',
  'collections/commentsCollection',
  'views/home/commentsView'
  
 
], function($, _, Backbone,Mustache,pTemplate , commentsCollection  , commentsView){



		 var activityView = Backbone.View.extend({ 
		 	tagName: "div",
		 
		    initialize: function(){
		    	
		      _.bindAll(this, 'render');
		    },
		    render: function(){
		    		$(this.el).html (  Mustache.to_html( pTemplate , this.model.toJSON())  );
		    		

		    		$(this.el).addClass("activityRow");


		    		$(this.el).append( this.model.get("object").content )



		    		//this.model.fetch();
		    		
		    		var $commentsCollection = new commentsCollection();

		    		var $commentsView = new commentsView({ collection: $commentsCollection });
		    		

		    		$(this.el).append($commentsView.el);

		    		console.log("commentsView.....")
		    		console.log($commentsView);
		    		console.log("collections commentsCollection");
		    		$commentsCollection.url = "http://localhost:5000/activity/"+this.model.id+"/comments";
		    		$commentsCollection.fetch( { reset:true, complete:function(){ 

		    			console.log("It's ok... ");
		    			console.log($commentsView);
		    			

		    		}});
		    		console.log($commentsCollection);	


		    	return this;
		    }


		 });


		 return activityView;
});

