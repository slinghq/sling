from sling import Application
from sling.core.logger import logger
from sling.ext import hello
import localmodule


app = Application([
    hello,
])


# Other way of installing a module
app.add_module(localmodule)


# Install a Falcon middleware
class HelloMiddleware(object):
    def process_request(self, req, res):
        logger.info('hellomiddleware processing request...')

    def process_resource(self, req, res, resource):
        logger.info('hellomiddleware processing resource...')

    def process_response(self, req, res, resource):
        logger.info('hellomiddleware processing response...')


app.add_middleware(HelloMiddleware)


# Install a standard WSGI Middleware
from werkzeug.contrib.profiler import ProfilerMiddleware
app.add_wsgi_middleware(
    ProfilerMiddleware, sort_by=('cumtime',), restrictions=('/opt', 30))

wsgi = app.wsgi


if __name__ == '__main__':
    app.manage()
