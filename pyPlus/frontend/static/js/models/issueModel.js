define([
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var issueModel = Backbone.Model.extend({
			 urlRoot: './api/issues',
			defaults: {
				id:null,
				name:null,
				description:null,
				order:null,
				csrf_token:null




			},

		});


		return issueModel;




});