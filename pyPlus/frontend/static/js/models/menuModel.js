define([
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var issueModel = Backbone.Model.extend({
			
			defaults: {
				id:null,
				name:null,
				




			},

		});


		return issueModel;




});