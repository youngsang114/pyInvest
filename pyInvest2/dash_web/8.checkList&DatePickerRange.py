import pandas as pd
from dash import Dash, html, dcc
from datetime import datetime

app = Dash()
app.layout = html.Div([

    # CheckList
    html.Br(),
    html.Br(),
    html.H3('CheckList'),
    dcc.Checklist(
        id = 'Check - List',
        options=[
            {'label': 'S&P500','value':'S&P 500'},
            {'label': 'KOSPI','value':'KOSPI'},
            {'label': 'KOSDAQ','value':'KOSDAQ'}
        ]
    ),

    html.Br(),
    html.Label('DatePickerRange'),
    dcc.DatePickerRange(id='DateRange',
                        start_date=datetime(2000,1,3),
                        end_date=datetime(2022,4,30),
                        min_date_allowed=datetime(2000,1,3),
                        max_date_allowed=datetime(2025,2,13))

])

if __name__ == '__main__':
    app.run_server()