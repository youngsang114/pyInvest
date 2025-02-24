from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
from datetime import datetime

def RSI(df, rsi_period):

    df_close_copy = df.copy()

    df_close_copy['Diff'] = df_close_copy.diff()
    df_close_copy['UP'] = np.where(df_close_copy['Diff'] >= 0 , df_close_copy['Diff'],0)
    df_close_copy['DOWN'] = np.where(df_close_copy['Diff'] < 0 , abs(df_close_copy['Diff']),0)
    df_close_copy['AU'] = df_close_copy['UP'].rolling(rsi_period).mean()
    df_close_copy['AD'] = df_close_copy['DOWN'].rolling(rsi_period).mean()
    df_close_copy['RS'] = df_close_copy['AU'] / df_close_copy['AD']
    df_close_copy['RSI'] = round(df_close_copy['RS'] / (1+df_close_copy['RS']) * 100,2)

    return df_close_copy[['RSI']]

def macdOscillator_fn(df, short_N, long_N, signal_N):

    df_close_copy = df.copy()
    df_close_copy['Short'] = df_close_copy[df_close_copy.columns[0]].ewm(span= short_N, adjust = False).mean()
    df_close_copy['Long'] = df_close_copy[df_close_copy.columns[0]].ewm(span= long_N, adjust = False).mean()
    df_close_copy['MACD'] = df_close_copy['Short'] - df_close_copy['Long']
    df_close_copy['Signal'] = df_close_copy['MACD'].ewm(span =signal_N, adjust=False).mean()
    df_close_copy['MACD Oscillator'] = df_close_copy['MACD'] - df_close_copy['Signal']

    return df_close_copy[['MACD','Signal', 'MACD Oscillator']]

## DataFrame & Set option

df_1 = pd.read_excel('C:\pyInvest\pyInvest2\Data\df_etf.xlsx', index_col=0,sheet_name='Sheet1')
df_2 = pd.read_excel('C:\pyInvest\pyInvest2\Data\df_etf.xlsx', index_col=0,sheet_name='Sheet2')
df_col_list = pd.read_excel('C:\pyInvest\pyInvest2\Data\df_etf.xlsx',sheet_name='Sheet3')

df=pd.concat([df_1,df_2],axis=1,join='outer')
df_copy = df.copy()

stock_index_col = df_col_list['Stock Index'].dropna().values
macro_index_col = df_col_list['Macro'].dropna().values
sector_index_col = df_col_list['Sector'].dropna().values

options_stock_index =[{'label':i,'value':i} for i in stock_index_col]
options_macro_index =[{'label':i,'value':i} for i in macro_index_col]
options_sector_index =[{'label':i,'value':i} for i in sector_index_col]


## Layout

app = Dash()
app.layout = html.Div([

    #### Layout1
    html.Div(id='Div1',
             children=[
                 html.H3('Stock Index DashBoard',style={'textAlign':'center'}),
                 html.Div(id='div1 input',
                          children=[
                              html.H5('Select ETF'),
                              dcc.Dropdown(id='div1 etf col',
                                           options=options_sector_index,
                                           multi=False,
                                           value='TIGER 200 금융',
                                           style={'fontSize':15,'width':'50%'}),
                              dcc.Input(id='div1 start date',
                                        value='20190101',
                                        style={'fontSize':15}),
                              dcc.Input(id='div1 end date',
                                        value='20200101',
                                        style={'fontSize':15}),
                              dcc.RadioItems(id='div1 radio items',
                                             options=[{'label':'RSI','value':'RSI'},{'label':'MACD','value':'MACD'}],
                                             value='MACD'),
                              html.Br(),
                              html.Button(id = 'div1 button',
                                          n_clicks=0,
                                          children='Submit',
                                          style={'fontSize':15})


                            
                          ]),
                 html.Div(id='div1 Graph',
                          children=[
                              dcc.Graph(id='div1 graph1'),
                              dcc.Graph(id= 'div1 graph2')
                          ]),
                 
             ],style={'display':'inline-block','width':'50%','verticalAlign':'top'}),

    #### Layout2         
    html.Div(id='Div2',
             children=[
                 html.H3('Macro Index DashBoard',style={'textAlign':'center'}),
                 html.Div(id='div2 input',
                          children=[
                              html.H5('Select ETF'),
                              dcc.Dropdown(id='div2 etf col',
                                           options=options_macro_index,
                                           multi=False,
                                           value='TIGER 구리실물',
                                           style={'fontSize':15,'width':'50%'}),
                              dcc.Input(id='div2 start date',
                                        value='20190101',
                                        style={'fontSize':15}),
                              dcc.Input(id='div2 end date',
                                        value='20200101',
                                        style={'fontSize':15}),
                              dcc.RadioItems(id='div2 radio items',
                                             options=[{'label':'RSI','value':'RSI'},{'label':'MACD','value':'MACD'}],
                                             value='MACD'),
                              html.Br(),
                              html.Button(id = 'div2 button',
                                          n_clicks=0,
                                          children='Submit',
                                          style={'fontSize':15})


                            
                          ]),
                 html.Div(id='div2 Graph',
                          children=[
                              dcc.Graph(id='div2 graph1'),
                              dcc.Graph(id= 'div2 graph2')
                          ]),

             ],style={'display':'inline-block','width':'50%','verticalAlign':'top'}),

    #### Layout3
    html.Div(id='Div3',
             children=[
                 html.H3('Return HeatMap', style={'textAlign':'center'}),
                 html.Div(id='div3 input',
                          children=[
                              html.H5('Select Index'),
                              dcc.RadioItems(id='div3 radio items',
                                             options=[{'label':'Stock Index','value':'Stock Index'},
                                                      {'label':'Macro','value':'Macro'},
                                                      {'label':'Sector','value':'Sector'}],
                                             value='Sector'),
                              html.Br(),
                              dcc.Input(id='div3 date',
                                        value='20190101',
                                        style={'fontSize':15}),
                              html.Br(),
                              html.Br(),
                              html.Button(id='div3 button',
                                          n_clicks=0,
                                          children='Submit',
                                          style={'fontSize':15})
                                        ]),
                 html.Br(),
                 html.Br(),
                 html.Div(id='div3 Graph',
                          children=[
                              html.Div(id='div3 date layout',
                                       children=['None']),
                              html.Br(),
                              dcc.Graph(id='div3 graph')
                          ])
             ],style={'display':'inline-block','width':'30%','verticalAlign':'top'}),
    #### Layout4
   
    html.Div(id = 'div4',
             children = [
                 html.H3('Macro & Sector', style = {'textAlign':'center'}),
                 html.Div(id = 'div4 input',
                          children = [
                              html.H5('Select Macro & Sector'),
                              dcc.Dropdown(id = 'div4 macro etf col',
                                           options = options_macro_index,
                                           multi = True,
                                           value = ['KODEX 콩선물(H)', 'KODEX 국채선물10년인버스'],
                                           style = {'width':'60%', 'fontSize':15}),
                              dcc.Dropdown(id = 'div4 sector etf col',
                                           options = options_sector_index,
                                           multi = True,
                                           value = ['TIGER 200 경기소비재', 'TIGER 200 금융'],
                                           style = {'width':'60%', 'fontSize':15}),
                              dcc.Input(id = 'div4 start date',
                                        value = '20210601',
                                        style = {'fontSize':15}),
                              dcc.Input(id = 'div4 end date',
                                        value = '20220101',
                                        style = {'fontSize':15}),
                              html.Br(),
                              html.Br(),
                              
                              html.Button(id = 'div4 button',
                                          n_clicks = 0,
                                          children = 'Submit',
                                          style = {'fontSize':15})
                                      ]),
                 dcc.Graph(id = 'div4 graph')
                 
                 ], style = {'display':'inline-block', 'width':'70%', 'verticalAlign':'top'})
    

])

#### Callback Functions

# Div1 callback function
@app.callback([Output('div1 graph1','figure'),
               Output('div1 graph2', 'figure')],
               [Input('div1 button','n_clicks')],
               [State('div1 etf col','value'),
                State('div1 start date','value'),
                State('div1 end date','value'),
                State('div1 radio items','value')])
def update_div1_graph(n_clicks, etf_col, start_date, end_date, radio_item):

    start=datetime.strptime(start_date,'%Y%m%d')
    end=datetime.strptime(end_date,'%Y%m%d')

    df_trace = df_copy.loc[start:end,[etf_col]].dropna()

    start_date_format = '{}Y-{}M-{}D'.format(df_trace.index[0].year,df_trace.index[0].month, df_trace.index[0].day)
    end_date_format = '{}Y-{}M-{}D'.format(df_trace.index[-1].year,df_trace.index[-1].month, df_trace.index[-1].day)

    trace1 = go.Scatter(x=df_trace.index,
                        y=df_trace[etf_col],
                        mode='lines')
    layout1 = go.Layout(title='{}'.format(etf_col),
                        xaxis={'title':'{} ~ {}'.format(start_date_format,end_date_format)},
                        yaxis={'tickformat' : ','})
    fig1 = go.Figure(trace1,layout1)
    fig1.update_layout(template='plotly_dark')

    if radio_item =='MACD':
        short_N = 9
        long_N = 26
        signal_N = 13
        df_macd = macdOscillator_fn(df=df_trace, short_N=short_N,long_N=long_N,signal_N=signal_N)

        trace2_1 = go.Scatter(x=df_macd.index,
                              y=df_macd['MACD'],
                              mode='lines',
                              name='MACD')
        trace2_2 = go.Scatter(x=df_macd.index,
                              y=df_macd['Signal'],
                              mode='lines',
                              name='Signal')
        trace2_3 = go.Scatter(x=df_macd.index,
                              y=df_macd['MACD Oscillator'],
                              mode='lines',
                              name='MACD Oscillator')
        layout2 = go.Layout(title='MACD')
        fig2 = go.Figure([trace2_1,trace2_2,trace2_3],layout2)
        fig2.update_layout(template='plotly_dark')
    else:
        df_rsi = RSI(df=df_trace, rsi_period=22)
        trace2_1 = go.Scatter(x=df_rsi.index,
                              y=df_rsi['RSI'],
                              mode='lines',
                              name='RSI')
        trace2_2 = go.Scatter(x=df_rsi.index,
                              y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*30,
                              line=dict(color='red',dash='dash'),
                              name='Lower Level')
        trace2_3 = go.Scatter(x=df_rsi.index,
                              y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*70,
                              line=dict(color='red',dash='dash'),
                              name='Upper Level')
        layout2 = go.Layout(title='RSI')
        fig2 = go.Figure([trace2_1,trace2_2,trace2_3],layout2)
        fig2.update_layout(template='plotly_dark')

    return fig1, fig2

# Div2 callback function

@app.callback([Output('div2 graph1','figure'),
               Output('div2 graph2', 'figure')],
               [Input('div2 button','n_clicks')],
               [State('div2 etf col','value'),
                State('div2 start date','value'),
                State('div2 end date','value'),
                State('div2 radio items','value')])
def update_div2_graph(n_clicks, etf_col, start_date, end_date, radio_item):

    start=datetime.strptime(start_date,'%Y%m%d')
    end=datetime.strptime(end_date,'%Y%m%d')

    df_trace = df_copy.loc[start:end,[etf_col]].dropna()

    start_date_format = '{}Y-{}M-{}D'.format(df_trace.index[0].year,df_trace.index[0].month, df_trace.index[0].day)
    end_date_format = '{}Y-{}M-{}D'.format(df_trace.index[-1].year,df_trace.index[-1].month, df_trace.index[-1].day)

    trace1 = go.Scatter(x=df_trace.index,
                        y=df_trace[etf_col],
                        mode='lines')
    layout1 = go.Layout(title='{}'.format(etf_col),
                        xaxis={'title':'{} ~ {}'.format(start_date_format,end_date_format)},
                        yaxis={'tickformat' : ','})
    fig1 = go.Figure(trace1,layout1)
    fig1.update_layout(template='plotly_dark')

    if radio_item =='MACD':
        short_N = 9
        long_N = 26
        signal_N = 13
        df_macd = macdOscillator_fn(df=df_trace, short_N=short_N,long_N=long_N,signal_N=signal_N)

        trace2_1 = go.Scatter(x=df_macd.index,
                              y=df_macd['MACD'],
                              mode='lines',
                              name='MACD')
        trace2_2 = go.Scatter(x=df_macd.index,
                              y=df_macd['Signal'],
                              mode='lines',
                              name='Signal')
        trace2_3 = go.Scatter(x=df_macd.index,
                              y=df_macd['MACD Oscillator'],
                              mode='lines',
                              name='MACD Oscillator')
        layout2 = go.Layout(title='MACD')
        fig2 = go.Figure([trace2_1,trace2_2,trace2_3],layout2)
        fig2.update_layout(template='plotly_dark')
    else:
        df_rsi = RSI(df=df_trace, rsi_period=22)
        trace2_1 = go.Scatter(x=df_rsi.index,
                              y=df_rsi['RSI'],
                              mode='lines',
                              name='RSI')
        trace2_2 = go.Scatter(x=df_rsi.index,
                              y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*30,
                              line=dict(color='red',dash='dash'),
                              name='Lower Level')
        trace2_3 = go.Scatter(x=df_rsi.index,
                              y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*70,
                              line=dict(color='red',dash='dash'),
                              name='Upper Level')
        layout2 = go.Layout(title='RSI')
        fig2 = go.Figure([trace2_1,trace2_2,trace2_3],layout2)
        fig2.update_layout(template='plotly_dark')

    return fig1, fig2

# Div3 callback function

# Div3 Callback Function
@app.callback([Output('div3 graph', 'figure'),
               Output('div3 date layout', 'children')],
              [Input('div3 button', 'n_clicks')],
              [State('div3 radio items', 'value'),
               State('div3 date', 'value')])
def update_div3_graph(n_clicks, radio_item, date):
    
    date_year = int(date[:4])
    date_month = int(date[4:6])
    date_day = int(date[6:8])
    date = datetime(date_year, date_month, date_day)
    
    if radio_item =='Stock Index':
        col_set = stock_index_col
    elif radio_item == 'Sector':
        col_set = sector_index_col
    elif radio_item == 'Macro':
        col_set = macro_index_col[:-1]
    
    df_trace = df_copy.loc[:date, col_set] ##
    
    date_format = '{}Y - {}M - {}D'.format(df_trace.index[-1].year, df_trace.index[-1].month, df_trace.index[-1].day)
    
    result_date_format = 'Reference Date: {}'.format(date_format)
    
    df_trace = df_trace.sort_index(ascending = False)
    
    daily_return  = round(df_trace.pct_change(periods = -1).iloc[0]*100, 1)
    weekly_return = round(df_trace.pct_change(periods = -5).iloc[0]*100, 1)
    monthly_return = round(df_trace.pct_change(periods = -22).iloc[0]*100, 1)
    
    ##### Make DataFrame of Return
    df_return = pd.DataFrame()
    
    df_return['Daily Return'] = daily_return
    df_return['Weekly Return'] = weekly_return
    df_return['Monthly Return'] = monthly_return
    
    #### Make HeatMap
    
    x = ['{}'.format(i) for i in df_return.columns]
    
    y = ['{}'.format(i) for i in df_return.index]
    
    z = df_return.values
    
    trace = ff.create_annotated_heatmap(z, x = x, y = y, colorscale = 'ylgnbu')
    
    layout = go.Layout(title = 'Heat Map of {}'.format(radio_item))
    
    fig = go.Figure(data = trace, layout = layout)
    
    fig.update_layout(
        autosize = False,
        width = 600,
        height = 900
        )
    
    return fig, result_date_format

# Div4 Callback Function
@app.callback(Output('div4 graph', 'figure'),
              [Input('div4 button', 'n_clicks')],
              [State('div4 macro etf col', 'value'),
               State('div4 sector etf col', 'value'),
               State('div4 start date', 'value'),
               State('div4 end date', 'value')])
def update_div4_graph(n_clicks, macro_col, sector_col, start_date, end_date):
    
    start_year = int(start_date[:4])
    start_month = int(start_date[4:6])
    start_day = int(start_date[6:8])
    start = datetime(start_year, start_month, start_day)
    
    end_year = int(end_date[:4])
    end_month = int(end_date[4:6])
    end_day = int(end_date[6:8])
    end = datetime(end_year, end_month, end_day)
    
    ### Set DataFrame
    
    col_list = macro_col + sector_col
    
    df_trace = df_copy.loc[start:end, col_list].dropna()
    
    start_date_format = '{}Y - {}M - {}D'.format(df_trace.index[0].year, df_trace.index[0].month, df_trace.index[0].day)
    end_date_format = '{}Y - {}M - {}D'.format(df_trace.index[-1].year, df_trace.index[-1].month, df_trace.index[-1].day)
    
    data = []
    
    for col in df_trace.columns:
        trace = go.Scatter(x = df_trace.index,
                           y = df_trace[col]/df_trace[col][0],
                           mode = 'lines',
                           name = '{}'.format(col))
        data.append(trace)
    
    layout = go.Layout(title = 'Macro & Sector Standard Price Graph',
                       xaxis = {'title':'{} ~ {}'.format(start_date_format, end_date_format)},
                       yaxis = {'tickformat':','})
    fig = go.Figure(data = data, layout = layout)
    fig.update_layout(template = 'plotly_dark')
    
    return fig



if __name__ == '__main__':
    app.run_server()