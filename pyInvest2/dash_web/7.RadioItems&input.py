import pandas as pd
from dash import Dash, html, dcc
import plotly.graph_objects as go


app=Dash()
app.layout = html.Div([

    #Input
    html.Br(),
    html.Label("Date Input"),
    html.Br(),
    dcc.Input(id="Start Date Input",
              value = 'Start Date'),
    dcc.Input(id="End Date Input",
              value = 'End Date'),
    # Radio Items
    html.Label('Radio Items'),   
    html.Br(),
    dcc.RadioItems(
        id = 'Radio Items',
        options= [
            {'label':'RSI','value':'RSI'},
            {'label':'MACD','value':'MACD'}
        ]
    )
    
    ])

    

if __name__ == '__main__':
    app.run_server()