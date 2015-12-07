from errors import *
from sling.core.command import Command
import falcon


class Application(object):

    def __init__(self):
        self.api = falcon.API()

    @property
    def wsgi(self):
        return self.api

    def manage(self):
        Command()


def create_app(modules=[]):
    app = Application()

    for module in modules:
        module.install_module(app)

    return app
