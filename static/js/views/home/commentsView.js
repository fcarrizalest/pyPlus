define([
'underscore',
'backbone',
 'views/home/commentView'
],function(_ , Backbone , commentView ){



			var peopleView = Backbone.View.extend( { 
					tagName: "ul",
					events: {
		       
		  			},
		  
		  			initialize: function(){	
	    		    	
	    		    	$(this.el).addClass("small-block-grid-1");
	    		    	$(this.el).addClass("medium-block-grid-2");
	    		    	$(this.el).addClass("large-block-grid-2");

	      				_.bindAll(this, 'addOne', 'addAll');
	        			this.collection.bind('reset', this.addAll);
	    			},
	    			addOne: function(op){
	    	
	    	
	    	 			var opView = new commentView({ model: op });
	    	    		this.opViews.push(opView);
	    	    	
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