define([
'underscore',
'backbone',
 'views/menu/menuitemView'
],function(_ , Backbone , activityView ){



			var peopleView = Backbone.View.extend( {

					events: {

		  			},

		  			initialize: function(){

	      				_.bindAll(this, 'addOne', 'addAll');
	        			this.collection.bind('reset', this.addAll);
	        			this.collection.bind('add', this.addAll);
	        			
	        			
	    			},
	    			addOne: function(op){

	    				console.log("Aqui tenemos uno");
	    				
	    	 			var opView = new activityView({ model: op });
	    	    		this.opViews.push(opView);
	    	    		$(this.el).append(opView.render().el);

	    			},
	    			addAll: function(){
	    				console.log("Entramos addAll menuItems")
	    	 			_.each(this.opViews,
	    		      		function(opView) { opView.remove(); });
	    		    	this.opViews = [];

	      				this.collection.each(this.addOne);
	    			}


			});

			return peopleView;



});