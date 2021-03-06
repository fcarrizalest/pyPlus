define([
'underscore',
'backbone',
 'views/home/issueView'
],function(_ , Backbone , activityView ){



			var peopleView = Backbone.View.extend( {

					events: {

		  			},

		  			initialize: function(){

	      				_.bindAll(this, 'addOne', 'addAll');
	        			this.collection.bind('reset', this.addAll);
	    			},
	    			addOne: function(op){


	    	 			var opView = new activityView({ model: op });
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