define([
'underscore',
'backbone',
'models/objectModel'
	], function( _, Backbone , issueModel){

			var activityCollection = Backbone.Collection.extend({

			model:issueModel,
			initialize: function( models , options ){


				this.on( "destroy" , this.destroyEvent , this)

			},
			destroyEvent:function(model, val, options){


					this.fetch( {reset:true});

			},

			parse: function(data){





				return data.data;
			},
			url : function() {
        		return "./api/objects/";
      		},



		});

		return activityCollection;



	 });