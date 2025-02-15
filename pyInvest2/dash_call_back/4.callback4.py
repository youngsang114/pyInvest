from dash import Dash, html, dcc
import numpy as np
import plotly.express as px
from dash.dependencies import Input,Output


app = Dash()
app.layout = html.Div([

    html.H4('Interactive scatter plot with Iris DataSet'),
    html.Br(),
    dcc.Graph(id ='graph'),
    html.Br(),
    html.P('Filter By petal width:'),
    dcc.RangeSlider(id = 'range-slider',
                    min = 0,
                    max =2.5,
                    step=0.1,
                    marks={0:'0',2.5:'2.5'},
                    value=[0.5,2])

])
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='range-slider',component_property='value')])
def update_graph(slider_range):

    df = px.data.iris()
    low,high = slider_range
    condition = (df['petal_width']>low) & (df['petal_width']<high)

    fig = px.scatter(df[condition],
                     x='sepal_width',
                     y='sepal_length',
                     color='species',
                     size='petal_length')
    return fig


if __name__ == '__main__':
    app.run_server()