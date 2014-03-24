define([
'underscore',
'backbone',
'models/menuModel'
	], function( _, Backbone , issueModel){

			var activityCollection = Backbone.Collection.extend({

			model:issueModel,
			initialize: function( models , options ){


				this.on( "destroy" , this.destroyEvent , this)

			},
			

			parse: function(data){





				return data.data;
			},
			


		});

		return activityCollection;



	 });