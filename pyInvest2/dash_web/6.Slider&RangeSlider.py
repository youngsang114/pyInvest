import pandas as pd
from dash import Dash, html, dcc
import plotly.graph_objects as go

# Slider

# app=Dash()
# app.layout = html.Div([

#     html.Label("Slider"),
#     html.Div(id = 'Slider',
             
#             children=[
#                 dcc.Slider(
#                     min =-5,
#                     max =10,
#                     step=1,
#                     marks = {i:i for i in range(-5,11)},
#                     value = 1
#                 )
#             ])
            
#     ])

# if __name__ == '__main__':
#     app.run_server()



# RangeSlider

app=Dash()
app.layout = html.Div([

    html.Br(),
    html.Label("Slider"),
    html.Br(),
    html.Div(id = 'Slider',
    
             
            children=[
                dcc.RangeSlider(
                    min =-5,
                    max =10,
                    step=1,
                    marks = {i:i for i in range(-5,11)},
                    value = [-2,4]
                )
            ])
            
    ])

if __name__ == '__main__':
    app.run_server()