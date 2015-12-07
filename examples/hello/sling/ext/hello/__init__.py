__version__ = '0.1.0'

from sling.core.g import g
from sling.core.logger import logger
import sling


class HelloResource(object):

    def on_get(self, req, res):
        logger.info('Saying hello as module...')
        res.body = "Hello! I'm ExampleModule."


def test_function(name):
    logger.info('Test function')


class HelloNameResource(object):

    def on_get(self, req, res, name):
        logger.info('Saying hello...')
        test_function(name)
        res.body = 'Hello, %s' % name
        logger.info('Said hello!')


def install_module(app):
    app.api.add_route('/hello', HelloResource())
    app.api.add_route('/hello/{name}', HelloNameResource())
    import command
