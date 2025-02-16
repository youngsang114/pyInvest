from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash()
app.layout = html.Div([

    html.H4('더하기 결과값'),
    dcc.Input(id='input1', type='text', value='', placeholder='단어1을 입력하세요'),
    html.Br(),
    html.Br(),
    dcc.Input(id='input2', type='text', value='', placeholder='단어2를 입력하세요'),
    html.Br(),

    html.Div(id='output_sum', children=['None'])  
])

@app.callback(
    Output('output_sum', 'children'),  
    [Input('input1', 'value'), Input('input2', 'value')]
)
def sum_fn(input1, input2):
    return input1 + input2 
if __name__ == '__main__':
    app.run_server()
