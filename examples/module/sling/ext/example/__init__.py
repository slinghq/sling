__version__ = '0.1.0'


class HelloResource(object):

    def on_get(self, req, res):
        res.body = "Hello! I'm ExampleModule."


hello_resource = HelloResource()


def install_module(app):
    app.api.add_route('/example', hello_resource)
