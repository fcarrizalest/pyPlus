define([
  'jquery',
  'underscore',
  'backbone',
  'mustache',
  'text!templates/home/pTemplate.html',
  'collections/activityCollection'
 
], function($, _, Backbone,Mustache,pTemplate , activityCollection){

	 var pView = Backbone.View.extend({
		    tagName: "div",
		 
		    initialize: function(){
		    	
		      _.bindAll(this, 'render');
		    },
		    render: function(){
		    	
		    	$(this.el).html (  Mustache.to_html( pTemplate , this.model.toJSON())  );
		      
		        //var t = $(this.el).find( "div").on( 'click' , { model : this.model } ,this.clickP);
		     	//console.log(t);
		     // $(this.el).attr('value',
		      //  this.model.get('id')).html(this.model.get('name'));
		      
		      return this;
		    },
		    events:{
		    	'click' : "clickP"
		    },
		    
		    clickP:function(e , model){
		    	var self = this;
		    	console.log("ID:")
		    	console.log(this.model.get('id') );
		    	var $id  = this.model.get('id');
		    	var $activityCollection = new activityCollection();

		    	console.log( $activityCollection);

		    	$activityCollection.url = './activities/'+$id ;


		    	this.activitiesView.collection = $activityCollection;

		    	$activityCollection.fetch( { reset:true , complete:function(){

		    		console.log("OK activities");
		    		console.log(this);
		    		self.activitiesView.addAll();

		    	}});
		    		
		    }
		  });

  return pView;
  
});