import os
from time import sleep

import dash_mantine_components as dmc
from dash import Dash, Output, Input, html
from flask_caching import Cache

app = Dash(__name__)
server = app.server

cache = Cache(
    app.server,
    config={
        "CACHE_TYPE": "RedisCache",
        "CACHE_REDIS_HOST": "redis",
        "CACHE_REDIS_PORT": os.environ["REDIS_PORT"],
    },
)

app.layout = dmc.Group(
    [
        dmc.Text("Dash-Docker"),
        dmc.NumberInput(id="number", value=1, min=1),
        html.Div(id="container"),
    ]
)


@app.callback(Output("container", "children"), Input("number", "value"))
@cache.memoize()
def update(value):
    if value and value >= 0:
        sleep(value)
        return value
    return "Enter valid number"
