from sling.core import command
import logging


logger = logging.getLogger('hello.command')


@command.command(name='hello:greet')
@command.argument('name')
def greet(name):
    """Greets hello to a name."""
    logger.debug('Greeting %s hello' % name)
    print 'Hello, %s' % name
    logger.debug('Done greeting!')
