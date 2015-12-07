import click


@click.group()
def Command():
    """Commands for this app."""


command = Command.command
option = click.option
argument = click.argument
