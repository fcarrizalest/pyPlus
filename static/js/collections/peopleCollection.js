define([
'underscore',
'backbone',
'models/peopleModel'
	], function( _, Backbone , peopleModel){
	 

		var peopleCollection = Backbone.Collection.extend({

			model:peopleModel,
			initialize: function( models , options ){},

			parse: function(data){

			

				return data.items;
			}



		});

		return peopleCollection;


});