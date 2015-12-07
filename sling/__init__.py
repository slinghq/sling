from falcon import API
from sling.core.command import Command


class Application(object):

    def __init__(self, modules=[], middlewares=[]):
        self.middlewares = []

        # Install core stuff
        self._enable_logger()

        # Installs user-provided middlewares
        for mid in middlewares:
            self.middlewares.append(m)

        # Instantiate api
        self.api = API(middleware=self.middlewares)

        # Install modules
        for mod in modules:
            mod.install_module(self)

    def _enable_logger(self):
        from sling.core import logger
        logger.install_module(self)

    @property
    def wsgi(self):
        return self.api

    def manage(self):
        Command()


def create_app(modules=[], middlewares=[], **kwargs):
    app = Application(
        modules=modules,
        middlewares=middlewares,
        **kwargs
    )
    return app


from errors import *
