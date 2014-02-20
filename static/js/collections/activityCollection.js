define([
'underscore',
'backbone',
'models/activityModel'
	], function( _, Backbone , activityModel){
	 
			var activityCollection = Backbone.Collection.extend({

			model:activityModel,
			initialize: function( models , options ){},

			parse: function(data){

				  

				

				return data.items;
			}



		});

		return activityCollection;



	 });