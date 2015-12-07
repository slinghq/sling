from sling.core import command


@command.command(name='hello:greet')
@command.argument('name')
def greet(name):
    """Greets hello to a name."""
    print 'Hello, %s' % name
