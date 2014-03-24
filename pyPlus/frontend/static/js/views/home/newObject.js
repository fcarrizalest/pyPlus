define([ 
	'jquery',
	'underscore',
	'backbone',
	'mustache',
	'text!templates/home/newObjectTemplate.html',
	'collections/issueCollection',
	'collections/categoryCollection',
	'views/home/categoriesView',
	'views/home/issuesView',
	'dropzone',
	'models/objectModel',
	

	] , function($,_ , Backbone,Mustache,homeTemplate,issueCollection,categoryCollection , categoriesView ,issuesView , dropzone , objectModel ) {
	
	
	var homeView = Backbone.View.extend( {

		el:$("#page"),
		initialize: function(){

			//_.bindAll(this)

			this.model = new objectModel();

		

		},
		render: function(){

			
			
			var issueC = new issueCollection();
			var categoriesC = new  categoryCollection();
			this.$el.html(  Mustache.to_html( homeTemplate , {type:this.type}) );
			
			var $categoriesView = new categoriesView({ el:$("#page").find("#newobjectCat") , collection: categoriesC });
			var $issuesView = new issuesView({ el:$("#page").find("#newobjectIss") , collection:issueC  });
			
			
			issueC.fetch( {  reset:true } );
			categoriesC.fetch( {  reset:true } );
			
			
			if( ( this.type == "Image" )  || (this.type == "Video" )){
				var $dropzone = new dropzone("#uploadZone",{
					  url:"/api/objects/upload",
					  
					  paramName: "file", // The name that will be used to transfer the file
					 
					  accept: function(file, done) {
					    if (file.name == "justinbieber.jpg") {
					      done("Naha, you don't.");
					    }
					    else { done(); }
					  }
					});
				
				var self = this;
				$dropzone.on("addedfile", function(file){
					console.log("Archivo subido");
					console.log(file);
					
					self.$el.find("#fileName").val(file.name);
					
					
				})
			}else{
				this.$el.find("#uploadZone").hide();
				
			}	

		},
		events:{
			"click .newO": "nuevo" ,

		},
		
		nuevo:function(){
			
			var $nombre = $("#nombre").val();
			var $newobjectIss = $("#newobjectIss").val();
			var $newobjectCat = $("#newobjectCat").val();
			var $desc = $("#desc").val();
			
			var $fileName = $("#fileName").val();
			
			this.model.set("name", $nombre);
			this.model.set("description", $desc);
			this.model.set("_typeO", this.type);
			this.model.set("issue", $newobjectIss);
			this.model.set("category", $newobjectCat);
			this.model.set("path", $fileName);
			
			console.log("click 3???")
			this.model.save();
			

		}
		

});



return homeView;
	
});