from flask_assets import Environment, Bundle


css_all = Bundle("css/estilos.css", filters="cssmin", output="css/estilos.min.css")

js_main = Bundle("js/libs/require/require.js", filters="jsmin", output="require.js")

def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
