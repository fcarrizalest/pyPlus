define([
	'underscore',
	'backbone',
	], function( _, Backbone ){

		var issueModel = Backbone.Model.extend({
			 urlRoot: './api/objects',
			defaults: {
				id:null,
				name:null,
				description:null,
				_typeO:null,
				issue : null,
				category : null,
				elemets : null,
				path : null,
				status : null,



			},

		});


		return issueModel;




});