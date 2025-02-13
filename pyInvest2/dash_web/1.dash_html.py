#Dash 모듈 불러오기

# from dash import Dash,html

# app = Dash()
# app.layout = html.Div([
#     html.Div(['Div1']),
#     html.Div(['Div2'])
# ])

# if __name__ == '__main__':
#     app.run_server()

# from dash import Dash, html

# app = Dash()
# app.layout = html.Div([

#     html.Div(id='Div1',
#              children = 'Div1입니다',
#              style= {'border':'red solid',
#                                 'textAlign':'center',
#                                 'display':'inline-block',
#                                 'fondtsize':20,
#                                 'width':'40%'}),

#     html.Div(id='Div1',
#              children = 'Div1입니다',
#              style= {'border':'green solid',
#                                'textAlign':'center',
#                                'display':'inline-block',
#                                'fontsize':20,
#                                'width':'45%'})


# ])

# if __name__ == '__main__':
#     app.run_server()

from dash import Dash, html

app = Dash()
app.layout = html.Div([

    html.Div(id='Layout1',
            children=[
                html.H1(id='H1', 
                        children='H1')
        ], style={'border':'blue solid'}),
    
    html.Br(),

    html.Div(id='Layout2',
            children=[
                html.H2(id='H2', 
                        children='H2')
        ], style={'border':'green solid'}),
    
    html.Br(),

    html.Div(id='Layout3',
            children=[
                html.H3(id='H3', 
                        children='H3')
        ], style={'border':'red solid'})

])

if __name__ == '__main__':
    app.run_server()