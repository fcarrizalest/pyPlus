define([ 
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var activityModel = Backbone.Model.extend({

			defaults: {  

				title:null,
				
				url:null,
				

			}, 
			url : function() {
        		return './activity/'+this.get('id');
      		},
		});


		return activityModel;




});
