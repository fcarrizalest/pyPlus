define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/home/pTemplate.html',
  'collections/activityCollection'
 
], function($, _, Backbone,Mustache,pTemplate , activityCollection){

	 var pView = Backbone.View.extend({
		    tagName: "li",
		 
		    initialize: function(){
		    	
		      _.bindAll(this, 'render');
		    },
		    render: function(){
		    	
		    	$(this.el).html (  Mustache.to_html( pTemplate , this.model.toJSON())  );
		      
		     
		      return this;
		    },
		    events:{
		    	'click' : "clickP"
		    },
		    
		    clickP:function(e , model){
		    	var self = this;
		    	
		    	var $id  = this.model.get('id');

		    	this.homeView.setPersonModel( this.model);
		    	var $activityCollection = new activityCollection();

		    	
		    	$activityCollection.url = './activities/'+$id ;


		    	this.activitiesView.collection = $activityCollection;

		    	$activityCollection.fetch( { reset:true , complete:function(){

		    		
		    		self.activitiesView.addAll();

		    	}});


		    		
		    }
		  });

  return pView;
  
});