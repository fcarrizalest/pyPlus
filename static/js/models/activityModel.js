define([ 
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var activityModel = Backbone.Model.extend({

			defaults: {  

				title:null,
				
				url:null,
				

			}

		});


		return activityModel;




});
