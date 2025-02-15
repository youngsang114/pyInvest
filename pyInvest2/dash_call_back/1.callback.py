from dash import Dash, html, dcc
from dash.dependencies import Input,Output

app = Dash()

app.layout = html.Div([

    # Input
    html.Label('Input layout'),
    dcc.Input(id='input',
              value='종목이름을 입력해주세요',
              type='text'),
    html.Br(),
    html.Label('Output Layout'),
    html.Div(id='div',
             children=['아직 아무것도 입력되지 않았습니다'])         
])
@app.callback(
        Output(component_id= 'div',
               component_property= 'children'),
        [Input(component_id='input',
               component_property='value')]

)
def update_layout_value(input_value):
    return "종목: {} 입력되었습니다.".format(input_value)

if __name__ =='__main__':
    app.run_server()