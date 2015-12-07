class IndexResource(object):

    def on_get(self, req, res):
        res.body = 'Hello. This is app.'


def install_module(app):
    """Installs this localmodule."""
    app.api.add_route('/', IndexResource())
