// Filename: router.js
define([
  'jquery',
  'underscore',
  'backbone',
  'views/home/homeView',
  'views/admin/homeView',
  'views/home/newObject',
  'views/menu/menuView',
  'collections/menuCollection'

], function($, _, Backbone, HomeView ,admin,newObject, menuView,menuCollection) {
  
  var AppRouter = Backbone.Router.extend({
    routes: {
    
      'admin' : 'adminHome',
      'new/:type'   : "newObject",
      // Default
      '*actions': 'defaultAction'
    }
  });
  
  
  var initialize = function(){
	  

    var app_router = new AppRouter;
    
    var $menuCollection = new menuCollection([ { name:"doosier1" , id:"123ff"} ]);
    
    var $menuView =  new menuView();
    $menuView.$menuCollection = $menuCollection;
    $menuView.render()
    
    
    app_router.on('route:newObject', function (type) {
    	var $newObject = new newObject();
    	console.log("parametro")
    	console.log(type)
    	$newObject.type = type;
    	
    	$newObject.render();
    	
    });
    
    app_router.on('route:defaultAction', function (actions) {
     
       // We have no matching route, lets display the home page 
        var homeView = new HomeView();
       
        homeView.render();     
        
//        $menuCollection.add([ { name:"doosier1" , id:"123ff"} ]);
//        $menuCollection.add([ { name:"doosier3" , id:"122ff"} ] );
//        
//        $menuCollection.trigger("add");
      
        
    });

    app_router.on( 'route:adminHome' , function(actions){


        var homeview = new admin();
      
        homeview.render();
        
       
       
        
    } );

    // Unlike the above, we don't call render on this view as it will handle
    // the render call internally after it loads data. Further more we load it
    // outside of an on-route function to have it loaded no matter which page is
    // loaded initially.
  //  var footerView = new FooterView();

    Backbone.history.start();
  };
  return { 
    initialize: initialize
  };
});