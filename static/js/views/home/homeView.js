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

					
					_.bindAll(this, 'clickBuscar')

					this.peopleCollection = new peopleCollection();

					this.onRequest = false;


				},
				render: function(){

					this.$el.html( homeTemplate );

					var $peopleView = new peopleView({ el:$("#personas")  , collection: this.peopleCollection });

					$peopleView.homeView =  this ;

					var $activityCollection = new activityCollection();

					var $activitiesView = new activitiesView( { el: $("#activity")  , collection: $activityCollection }) ;

					$peopleView.activitiesView = $activitiesView;


					this.clickBuscar();

				},
				events:{
					"click button": "clickBuscar",
					"keyup #buscar" : "keypressBuscar"

				},
				setPersonModel: function( $model){

					console.log("persona");
					console.log( $model );

				},
				clickBuscar: function(){

					console.log("Buscar........???");

					this.peopleCollection.url = "./search/p/"+$("#buscar").val();
					this.peopleCollection.fetch( {  reset:true } );
					$("#activity").html(" ");
				},
				keypressBuscar:function(e){

				


					this.peopleCollection.url = "./search/p/"+e.currentTarget.value;
					$self = this;
					if( !this.onRequest){
						$("#activity").html(" ");
						this.onRequest = true;
						this.peopleCollection.fetch( {  reset:true , complete:function(){

								$self.onRequest = false;

						} })
					}

				}


		});



		return homeView;


});