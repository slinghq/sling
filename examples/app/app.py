from sling import create_app
from sling.ext import hello
import localmodule


app = create_app([
    hello,
    localmodule,
])
wsgi = app.wsgi


if __name__ == '__main__':
    app.manage()
