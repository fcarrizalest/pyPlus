define([ 
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var commentModel = Backbone.Model.extend({

			defaults: {  

				title:null,
				published:null,
				updated:null,
				url:null,
				actor:null,
				object:null,

			}, 
			url : function() {
        		return './activity/'+this.get('id');
      		},
		});


		return commentModel;




});
