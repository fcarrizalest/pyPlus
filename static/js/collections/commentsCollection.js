define([
'underscore',
'backbone',
'models/commentModel'
	], function( _, Backbone , commentModel){ 

		var commentCollection = Backbone.Collection.extend({

			model:commentModel,
			initialize: function( models , options ){},

			parse: function(data){
					

				return data.items;
			}



		});

		return commentCollection;



});