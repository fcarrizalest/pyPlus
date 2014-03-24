// Author: fcarrizalest
// Filename: main.js

// Require.js allows us to configure shortcut alias
// Their usage will become more apparent futher along in the tutorial.
require.config({
 
  config: { 'waitSeconds':100 },
  paths: {
    jquery: 'libs/jquery/jquery',
    underscore: 'libs/underscore/underscore',
    backbone: 'libs/backbone/backbone',
    mustache: 'libs/mustache/mustache',
    dropzone: 'vendor/dropzone.min',
    templates: '../templates'
  }

});


require([
  // Load our app module and pass it to our definition function
  'app',
  
], function(App  ){
	
	
	
  // The "app" dependency is passed in as "App"
  // Again, the other dependencies passed in are not "AMD" therefore don't pass a parameter to this function
  App.initialize();
});