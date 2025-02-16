from dash import Dash, html, dcc
from dash.dependencies import Input,Output,State

app = Dash()
app.layout = html.Div([
    
    html.Br(),
    html.Br(),
    dcc.Input(id='input',
              value=1,
              style={'fontsize':20}),
    html.Button(id ='button',
                n_clicks=0,
                children='Summit',
                style={'fontsize':20}),
    html.Br(),
    html.Label('Output'),
    html.Div(id='div')

])
@app.callback(
        Output(component_id='div',component_property='children'),
        [Input(component_id='button',component_property='n_clicks')],
        [State(component_id='input',component_property='value')]
)
def update_div(n_clicks,input_value):
    return 'Input word : {} & Clicks : {}'.format(input_value,n_clicks)


if __name__ =='__main__':
    app.run_server()
