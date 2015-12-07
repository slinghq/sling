from sling import create_app
from sling.ext import example
import localmodule


app = create_app([
    example,
    localmodule,
])
wsgi = app.wsgi


if __name__ == '__main__':
    app.manage()
