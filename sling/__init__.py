import falcon


def create_app(modules=[]):
    app = falcon.API()

    for module in modules:
        module.install_module(app)

    return app
