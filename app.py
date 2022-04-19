from time import sleep

from dash import Dash, Output, Input, html
import dash_mantine_components as dmc

from flask_caching import Cache

app = Dash(__name__)
cache = Cache(
    app.server,
    config={
        "CACHE_TYPE": "RedisCache",
        "CACHE_REDIS_HOST": "redis",
        "CACHE_REDIS_PORT": 6379,
    },
)

app.layout = dmc.Group(
    [
        dmc.NumberInput(id="number", min=1),
        html.Div(id="container"),
    ]
)


@app.callback(
    Output("container", "children"), Input("number", "value"), prevent_initial_call=True
)
@cache.memoize()
def update(value):
    if value and value >= 0:
        sleep(value)
        return value
    return "Enter valid number"


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
