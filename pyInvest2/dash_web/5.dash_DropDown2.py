import pandas as pd
from dash import Dash, html, dcc
import plotly.graph_objects as go

df = pd.read_excel('./pyInvest2/Data/df_etf.xlsx', index_col=0)

kind = 'KODEX'
condition = [df.columns[i] for i in range(df.shape[1]) if kind in df.columns[i]]

app = Dash()
app.layout = html.Div([

    html.Label('ETF DropDown'),
    html.Div(id='ETF DropDown',
             children=[
                 dcc.Dropdown(
                    options=[{'label':'{}'.format(i), 'value':'{}'.format(i)} for i in condition],
                    # value= '002380',
                    placeholder='ETF를 선택해주세요'
                 )
                ],
                style={'width':'35%'})

])

if __name__ == '__main__':
    app.run_server()