from sling import create_app
from sling.ext import example


app = create_app(
    modules=[
        example,
    ]
)
