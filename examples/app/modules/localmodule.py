class LocalModule(object):

    def on_get(self, req, resp):
        resp.body = "Hello! I'm LocalModule."


local_module = LocalModule()


def install_module(app):
    app.add_route('/', local_module)
