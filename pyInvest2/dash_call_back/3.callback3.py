from dash import Dash, html, dcc
import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Input,Output

app = Dash()
app.layout = html.Div([

    html.Label("Input Random Number"),
    dcc.Input(id='input',
              value='5'),
    html.Br(),
    dcc.Graph(id='graph'),
    html.Br(),
    html.Label('Random X avg'),
    html.Div(id='summary div',
             children=['None'])

])
@app.callback(
        Output(component_id='graph', component_property='figure'),
        [Input(component_id='input',component_property='value')]
)
def random_fig(n):
    n = int(n)

    random_x = np.random.randint(0,300,n)
    random_y = np.random.randint(0,100,n)

    trace1= go.Scatter(x=random_x,
                      y=random_y,
                      mode='markers',
                      marker={'size':15},
                      name='Random Number')
    
    random_x_avg = [np.sum(random_x)/n]
    random_y_avg = [np.sum(random_y)/n]

    trace2 = go.Scatter(x=random_x_avg,
                        y=random_y_avg,
                        mode='markers',
                        marker={'size':20,'color':'Red'},
                        name='Random Avg X : {} & Y : {}'.format(random_x_avg,random_y_avg))
    
    layout = go.Layout(title='Random Number Graph N {}'.format(n))
    fig = go.Figure([trace1,trace2],layout)
    return fig

@app.callback(
        Output(component_id='summary div', component_property='children'),
        [Input(component_id='input',component_property='value')]
)
def random_x_avg(n):

    n = int(n)
    random_x = np.random.randint(0,300,n)
    random_x_avg = [np.sum(random_x)/n]
    return random_x_avg

if __name__ =='__main__':
    app.run_server()