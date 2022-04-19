from dash import Dash
from dash_mantine_components import Button

app = Dash(__name__)

app.layout = Button("This is a button")

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
