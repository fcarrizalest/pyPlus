define([ 
	'jquery',
	'underscore',
	'backbone',
	'text!templates/admin/homeTemplate.html',
		] , function($,_ , Backbone,homeTemplate ){



			var homeView = Backbone.View.extend( {

				el:$("#page"),
				initialize: function(){


				},
				render: function(){

					this.$el.html( homeTemplate );
				}
			});


			return homeView


});