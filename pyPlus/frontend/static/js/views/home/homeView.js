define([ 
	'jquery',
	'underscore',
	'backbone',
	'text!templates/home/homeTemplate.html',
	

	] , function($,_ , Backbone,homeTemplate  ) {   




		var homeView = Backbone.View.extend( {

				el:$("#page"),
				initialize: function(){

					//_.bindAll(this)

					



				},
				render: function(){

					this.$el.html( homeTemplate );

					 $(document).foundation();


				},
				events:{
				

				},
				

		});



		return homeView;


});