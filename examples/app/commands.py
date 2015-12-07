from sling.core import command


@command.command(name='example:greet')
@command.argument('name')
def greet(name):
    """Greets hello to a person."""
    print 'Hello, %s' % name
