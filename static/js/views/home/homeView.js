define([ 
	'jquery',
	'underscore',
	'backbone',
	'text!templates/home/homeTemplate.html',
	'collections/peopleCollection',
	'views/home/peopleView',
	'views/home/activitiesView',
	'collections/activityCollection'

	] , function($,_ , Backbone,homeTemplate , peopleCollection ,peopleView , activitiesView , activityCollection) {   




		var homeView = Backbone.View.extend( {

				el:$("#page"),
				initialize: function(){

					console.log("OK ---- HomeView");
					_.bindAll(this, 'clickBuscar')

					this.peopleCollection = new peopleCollection();



				},
				render: function(){

					this.$el.html( homeTemplate );

					var $peopleView = new peopleView({ el:$("#personas")  , collection: this.peopleCollection });

					var $activityCollection = new activityCollection();

					var $activitiesView = new activitiesView( { el: $("#activity")  , collection: $activityCollection }) ;

					$peopleView.activitiesView = $activitiesView;


				},
				events:{
					"click button": "clickBuscar",
					"keyup #buscar" : "keypressBuscar"

				},
				clickBuscar: function(){

					console.log("Buscar........???");

				},
				keypressBuscar:function(e){

					console.log ( e.currentTarget.value );


					this.peopleCollection.url = "./search/p/"+e.currentTarget.value;

					this.peopleCollection.fetch( {  reset:true , complete:function(){

						console.log( this.length);

					} })

				}


		});



		return homeView;


});