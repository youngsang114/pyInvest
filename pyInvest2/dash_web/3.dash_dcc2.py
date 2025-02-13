from dash import Dash, html, dcc
import numpy as np
import plotly.graph_objects as go

random_x1 = np.random.randint(0,100,50)
random_y1 = np.random.randint(0,100,50)

trace1 = go.Scatter(x=random_x1,
                   y=random_y1,
                   mode='markers',
                   marker={'size':12,
                           'color':'rgb(50,203,153)',
                           'symbol':'pentagon',
                           'line':{'width':2}})
random_x2 = np.random.randint(0,100,50)
random_y2 = np.random.randint(0,100,50)

trace2 = go.Scatter(x=random_x2,
                   y=random_y2,
                   mode='markers',
                   marker={'size':12,
                           'color':'rgb(153,203,53)',
                           'symbol':'pentagon',
                           'line':{'width':2}})

layout = go.Layout(title='Random Variable Scatter Plot',
                   xaxis={'title':'random X'},
                   yaxis={'title':'random Y'})

fig1 = go.Figure(data=trace1, layout=layout)
fig2 = go.Figure(data=trace2, layout=layout)

app = Dash()
app.layout = html.Div([

    html.Div(id = 'Div1',
              children =[
                  dcc.Graph(id='Random Variable Scatter Plot1',
                  figure= fig1)
    ]),
    html.Div(id = 'Div2',
              children =[
                  dcc.Graph(id='Random Variable Scatter Plot2',
                  figure= fig2)
    ])    
])

if __name__ == '__main__':
    app.run_server()