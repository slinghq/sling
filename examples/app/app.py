from sling import create_app
from sling.ext import example
from modules import localmodule


app = create_app(
    modules=[
        example,
        localmodule,
    ]
)
