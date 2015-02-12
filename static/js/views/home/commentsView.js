define([
'underscore',
'backbone',
 'views/home/commentView'
],function(_ , Backbone , commentView ){



			var peopleView = Backbone.View.extend( { 
					tagName: "fieldset",
					events: {
		       
		  			},
		  
		  			initialize: function(){	
	    		    	
	      				_.bindAll(this, 'addOne', 'addAll');
	        			this.collection.bind('reset', this.addAll);
	    			},
	    			addOne: function(op){
	    	
	    	
	    	 			var opView = new commentView({ model: op });
	    	    		this.opViews.push(opView);
	    	    		console.log("Render subview");
	    	    		console.log(opView.render());
	    	    		console.log($(this));
	    	    		$(this.el).append(opView.render().el);
	 
	    			},
	    			addAll: function(){
	    	
	    	 			_.each(this.opViews,
	    		      		function(opView) { opView.remove(); });
	    		    	this.opViews = [];
	    		    
	      				this.collection.each(this.addOne);
	    			}


			});

			return peopleView;



});