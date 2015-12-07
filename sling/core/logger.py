from sling.core import config
from sling.core.g import g
import sys
import logging


class TransactionIdLogFilter(logging.Filter):

    def filter(self, record):
        record.transaction_id = g.transaction_id
        return True


class TransactionIdMiddleware(object):

    def process_request(self, req, res):
        g.generate_transaction_id()

    def process_resource(self, req, res, resource):
        pass

    def process_response(self, req, res, resource):
        g.clear_transaction_id()


formatter = logging.Formatter(config.LOG_FORMAT, datefmt=config.LOG_TIMESTAMP_FORMAT)
handler = logging.StreamHandler(sys.stdout, )
logger = logging.getLogger('sling')
logger.setLevel(config.LOG_LEVEL)
handler.setFormatter(formatter)
handler.addFilter(TransactionIdLogFilter())
logger.addHandler(handler)


def install_module(app):
    app.middlewares.append(TransactionIdMiddleware())
