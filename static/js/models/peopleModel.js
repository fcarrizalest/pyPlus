define([ 
	'underscore',
	'backbone',
	], function( _, Backbone ){


		var peopleModel = Backbone.Model.extend({
 
			defaults: {  

				kind:null,
				displayName:null,
				url:null,
				image:null

			}

		});


		return peopleModel;




});

