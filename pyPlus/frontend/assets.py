from flask_assets import Environment, Bundle


css_all = Bundle(   "css/foundation.css", "css/estilos.css" , "css/basic.css" , "css/dropzone.css", filters="cssmin", output="css/estilos.min.css")

js_header  = Bundle(  "js/vendor/modernizr.js" , filters="jsmin", output="modernizr.js" ) 

js_main = Bundle("js/libs/require/require.js",   "js/vendor/jquery.js" ,"js/foundation.min.js" , "js/foundation/foundation.tab.js",  filters="jsmin", output="require.js")



def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_header', js_header)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
