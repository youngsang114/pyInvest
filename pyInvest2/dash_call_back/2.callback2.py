from dash import Dash, html, dcc
import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Output, Input


app = Dash()
app.layout = html.Div([

    html.Label("Input Random Number"),
    
    html.Div(id = 'Input Div',
             children=[
                dcc.Input(id = 'input',
                value=5)]),
    html.Br(),
    html.Br(),
    dcc.Graph(id='graph')

])

@app.callback(
        Output(component_id='graph',
               component_property='figure'),
        [Input(component_id='input',
               component_property='value')]
)
def random_scatter(num):
    num = int(num) # 문자열로 받아짐 -> int형으로 바꿔주기
    x_random = np.random.randint(0,500,num)
    y_random = np.random.randint(0,1500,num)

    data=go.Scatter(x=x_random,
                    y=y_random,
                    mode='markers',
                    name='Random Number')
    layout=go.Layout(title='Random Number Graph N :{}'.format(num),
                   xaxis={'title':'random X'},
                   yaxis={'title':'random Y'})
    fig = go.Figure(data=data,layout=layout)
    return fig


if __name__ == '__main__':
    app.run_server()