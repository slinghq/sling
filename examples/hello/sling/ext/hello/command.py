from sling.core import command
from sling.core.logger import logger


logger = logger.getChild('hello.command')


@command.command(name='hello:greet')
@command.argument('name')
def greet(name):
    """Greets hello to a name."""
    greet_logger = logger.getChild(name)
    greet_logger.debug('Greeting %s hello' % name)
    print 'Hello, %s' % name
    greet_logger.debug('Done greeting!')
