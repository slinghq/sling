from falcon import api_helpers as falcon_helpers
import falcon


class Application(object):

    def __init__(self, modules=[], *args, **kwargs):
        self.modules = []
        self.middlewares = []
        self.wsgi_middlewares = []
        self._is_prepared = False
        self.api = falcon.API()


        # Install core modules
        from sling.core import logger
        self.add_module(logger)
        # XXX: We flush the core modules immidately before the user defined
        # modules to guarantee order of propagation of middlewares,
        # wsgi_middlewares and so on.
        self._install_modules()

        # Install user-defined modules
        for module in modules:
            self.add_module(module)

    def _prepare_api(self):
        if self._is_prepared is False:
            # Install modules here.
            self._install_modules()
            # Apply falcon middlewares here.
            self._install_middlewares()
            self._is_prepared = True

    @property
    def wsgi(self):
        # Prepare application first.
        self._prepare_api()
        # Apply wsgi middlewares here.
        app = self.api
        app = self._install_wsgi_middlewares(app)
        return app

    def _install_middlewares(self):
        middlewares = [m(*margs, **mkwargs) for m, margs, mkwargs in self.middlewares]
        self.api._middleware = falcon_helpers.prepare_middleware(middlewares)

    def _install_wsgi_middlewares(self, app):
        for m, margs, mkwargs in self.wsgi_middlewares:
            app = m(app, *margs, **mkwargs)
        return app

    def _install_modules(self):
        for m, margs, mkwargs in self.modules:
            m.install_module(self, *margs, **mkwargs)
        self.modules[:] = []

    def add_module(self, module, *args, **kwargs):
        self.modules.append((module, args, kwargs))

    def add_wsgi_middleware(self, middleware, *args, **kwargs):
        self.wsgi_middlewares.append((middleware, args, kwargs))

    def add_middleware(self, middleware, *args, **kwargs):
        self.middlewares.append((middleware, args, kwargs))

    def manage(self):
        from sling.core.command import Command
        Command()
