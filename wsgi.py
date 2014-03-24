# -*- coding: utf-8 -*-
import os, sys; sys.path.append(os.path.dirname(__file__))

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from pyPlus import frontend, admin


application = DispatcherMiddleware(frontend.create_app() , {
    '/api': admin.create_app()
})
if __name__ == "__main__":
    run_simple('0.0.0.0', 5004, application, use_reloader=True, use_debugger=False)
