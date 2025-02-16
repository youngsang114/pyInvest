from dash import Dash, html, dcc
from dash.dependencies import Input,Output,State
import plotly.graph_objects as go
import numpy as np

app = Dash()
app.layout = html.Div([
    
    html.H1('Random Number Input'),
    html.Br(),
    html.Br(),

    html.H4('Input Lower Bound'),
    dcc.Input(id='input1', value=1),
    
    html.H4('Input Upper Bound'),
    dcc.Input(id='input2', value=1000),

    html.Br(),
    html.Br(),
    html.H4('Input Random Number'),
    dcc.Input(id='input3',value=200),
    html.Br(),
    html.Button(id ='button',
                n_clicks=0,
                children='Summit',
                style={'fontsize':20}),

    html.Br(),
    dcc.Graph(id = 'graph')
])

@app.callback(Output(component_id='graph',component_property='figure'),
              [Input(component_id='button',component_property='n_clicks')],
              [State(component_id='input1',component_property='value'),
               State(component_id='input2',component_property='value'),
               State(component_id='input3',component_property='value')])

def random_scatter(n_clicks,lower, upper, n):

    lower, upper, n=int(lower), int(upper), int(n)

    x_random=np.random.randint(lower,upper,n)
    y_random=np.random.randint(lower,upper,n)

    data=go.Scatter(x=x_random,
               y=y_random,
               mode='markers',
               name='Random Number')
               
    layout=go.Layout(title='Variables')
    fig = go.Figure(data=data,layout=layout)
    return fig


if __name__ =='__main__':
    app.run_server()
