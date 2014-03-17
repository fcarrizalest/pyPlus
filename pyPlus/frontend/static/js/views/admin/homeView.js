define([
	'jquery',
	'underscore',
	'backbone',
	'text!templates/admin/homeTemplate.html',
	'views/admin/issuesView',
	'collections/issueCollection'
		] , function($,_ , Backbone,homeTemplate , issuesView , issueCollection ){



			var homeView = Backbone.View.extend( {

				el:$("#page"),
				initialize: function(){
					this.issueC = new issueCollection();

				},
				render: function(){



					this.$el.html( homeTemplate );




					var $issuesView = new issuesView({ el:$("#Issues")  , collection: this.issueC });

					this.issueC.fetch( {  reset:true } );

				},
				events:{
					"click #addIssue": "AddIssue",
				},
				AddIssue:function(){
					var iname = $("#Iname").val()
					var Idescription = $("#Idescription").val()
					var csrf_token = $('meta[name=csrf_token]').attr("content");
					var self = this;
					$.post( "./api/issues/" , { name:iname , description:Idescription , csrf_token:csrf_token , order: 10 } , function(){} , "json" ).done(function() {

    						self.issueC.fetch( {  reset:true } );

    						$("#Iname").val("")
    						$("#Idescription").val("")
  					})

				}
			});


			return homeView


});