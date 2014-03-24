define([ 
	'jquery',
	'underscore',
	'backbone',
	'text!templates/menu/menuTemplate.html',
	'views/menu/menuItemsView',
	

	] , function($,_ , Backbone,homeTemplate ,menuItemsView ) {   




		var homeView = Backbone.View.extend( {

				el:$("#menu"),
				initialize: function(){

					//_.bindAll(this)

					



				},
				render: function(){

					this.$el.html( homeTemplate );

					var $menuItemsView = new menuItemsView( { el:$("#dMenu")   , collection: this.$menuCollection })
					
					

				},
				events:{
				

				},
				

		});



		return homeView;


});