__version__ = '0.1.0'


class HelloResource(object):

    def on_get(self, req, res):
        res.body = 'Hello'


hello_resource = HelloResource()


def install_module(app):
    app.add_route('/example', hello_resource)
