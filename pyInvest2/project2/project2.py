from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from sklearn import linear_model
from statsmodels.tsa.stattools import adfuller

def adf_test(df,critical_value):
    p_value = adfuller(df)[1]
    
    if p_value < critical_value:
        return 'P-Value : {} & Time Series Data is Stationary'.format(round(p_value,3))
    else:
        return 'P-Value : {} & Time Series Data is Non-Stationary'.format(round(p_value,3))

def signal_level(spread, z_score):
    mean = spread.mean()
    std = spread.std()

    return z_score*std + mean

df = pd.read_excel("C:\pyInvest\pyInvest2\Data\df_etf.xlsx",index_col=0)
df_copy=df.copy()

condition_kodex = [df_copy.columns[i] for i in range(df_copy.shape[1]) if 'KODEX' in df_copy.columns[i]]
df_copy_kodex=df_copy.loc[:,condition_kodex]

options = [{'label': i, 'value': i} for i in df_copy_kodex.columns]

app = Dash()
app.layout = html.Div([
    
    html.Br(),
    html.H1('Pair Trading DashBoard'),
    html.Div(id = 'layout div title',
             children=[
                html.H3('Select ETF', style={'paddingRight':'30px'}),
                dcc.Dropdown(id='etf_col',
                             options=options,
                             multi=True,
                             value=['KODEX 코스피', 'KODEX 코스닥150'],
                             style={'width': '60%', 'fontSize':18})
             ]),
    html.Div(id='laout input',
             children=[
                html.Div(id='div data',
                          children=[
                              html.P('Input Start Date & End Date'),
                              dcc.Input(id = 'startDate',
                                        value='20180101',
                                        style={'fontSize':15}),
                              dcc.Input(id = 'endDate',
                                        value='20200101',
                                        style={'fontSize':15})
                            
                          ],
                          style={'display':'inline-block', 'verticalAlign':'top','width':'30%'}),
                html.Div(id ='div critical value',
                         children=[
                             html.P('Input Critical Value'),
                             dcc.Input(id ='critical value',
                                       value=0.05,
                                       style={'fontSize':15})
                         ],
                         style={'display':'inline-block', 'verticalAlign':'top','width':'30%'}),
                html.Div(id ='div z_score',
                         children=[
                             html.P('Input z_score'),
                             dcc.Input(id ='z_score',
                                       value=1.65,
                                       style={'fontSize':15})
                         ],
                         style={'display':'inline-block', 'verticalAlign':'top','width':'30%'})
             ]),
    html.Br(),
    html.Br(),
    html.Div(id='layout button',
            children= [
                html.Button(id='button',
                            n_clicks=0,
                            children='Submit',
                            style={'fontSize':15})
                        ]),
    
    html.Div(id='etf graph',
             children=[
                 dcc.Graph(id ='etf 1',
                 style={'display':'inline-block','width':'50%'}),
                 dcc.Graph(id='etf 2',
                 style={'display':'inline-block','width':'50%'})
             ]),
    dcc.Graph(id='standard price graph'),
    dcc.Graph(id='trading graph')

])

@app.callback([Output(component_id='etf 1',component_property='figure'),
               Output(component_id='etf 2',component_property='figure'),
               Output(component_id='standard price graph',component_property='figure'),
               Output(component_id='trading graph',component_property='figure')],
               [Input(component_id='button', component_property='n_clicks')],
               [State(component_id='etf_col',component_property='value'),
                State(component_id='startDate',component_property='value'),
                State(component_id='endDate',component_property='value'),
                State(component_id='critical value',component_property='value'),
                State(component_id='z_score',component_property='value')])
def update_figure(n_clicks,etf_col,start_date,end_date,crtical_value,z_score):

    start=datetime.strptime(start_date,'%Y%m%d')
    end=datetime.strptime(end_date,'%Y%m%d')

    crtical_value = float(crtical_value)
    z_score = float(z_score)

    df_trace = pd.DataFrame()

    for col in etf_col:
        df_trace['{}'.format(col)] = df_copy_kodex.loc[start:end,col]
    
    df_trace = df_trace.dropna()
    df_trace['Standard Price of {}'.format(df_trace.columns[0])] = df_trace[df_trace.columns[0]]/df_trace[df_trace.columns[0]].iloc[0]
    df_trace['Standard Price of {}'.format(df_trace.columns[1])] = df_trace[df_trace.columns[1]]/df_trace[df_trace.columns[1]].iloc[0]

    start_date_format = '{}Y-{}M-{}D'.format(df_trace.index[0].year,df_trace.index[0].month, df_trace.index[0].day)
    end_date_format = '{}Y-{}M-{}D'.format(df_trace.index[-1].year,df_trace.index[-1].month, df_trace.index[-1].day)

    ## Pair Trading Component

    X = df_trace[[df_trace.columns[1]]]
    y = df_trace[[df_trace.columns[0]]]

    model = linear_model.LinearRegression(fit_intercept=False)
    model.fit(X=X,y=y)

    spread = df_trace[df_trace.columns[0]] - model.coef_[0]*df_trace[df_trace.columns[1]]

    result_stationary = adf_test(df=spread, critical_value=crtical_value)
    data_mean = [spread.mean() for i in range(spread.shape[0])]

    upper_level = signal_level(spread=spread,z_score=z_score)
    lower_level = signal_level(spread=spread, z_score=-z_score)

    data_upper_level = [upper_level for i in range(spread.shape[0])]
    data_lower_level = [lower_level for i in range(spread.shape[0])]

    ## Figure Update

    trace1 = go.Scatter(x=df_trace.index,
                        y=df_trace[df_trace.columns[0]],
                        mode='lines')
    layout1 = go.Layout(title='{}'.format(df_trace.columns[0]),
                        xaxis={'title':'{} ~ {}'.format(start_date_format,end_date_format)},
                        yaxis={'tickformat' : ','})
    fig1 = go.Figure(trace1,layout1)
    fig1.update_layout(template='ggplot2')

    trace2 = go.Scatter(x=df_trace.index,
                        y=df_trace[df_trace.columns[1]],
                        mode='lines')
    layout2 = go.Layout(title='{}'.format(df_trace.columns[1]),
                        xaxis={'title':'{} ~ {}'.format(start_date_format,end_date_format)},
                        yaxis={'tickformat' : ','})
    fig2 = go.Figure(trace2,layout2)
    fig2.update_layout(template='ggplot2')

    trace3_1 = go.Scatter(x=df_trace.index,
                        y=df_trace[df_trace.columns[2]],
                        mode='lines',
                        name='{}'.format(df_trace.columns[2]))
    trace3_2 = go.Scatter(x=df_trace.index,
                        y=df_trace[df_trace.columns[3]],
                        mode='lines',
                        name='{}'.format(df_trace.columns[3]))
    layout3 = go.Layout(title='Standard Price of {} & {}'.format(df_trace.columns[0],df_trace.columns[1]),
                        xaxis={'title':'{} ~ {}'.format(start_date_format,end_date_format)},
                        yaxis={'tickformat' : ','})
    fig3 = go.Figure(data=[trace3_1,trace3_2],layout=layout3)
    fig3.update_layout(template='plotly_white')

    fig4_1 = go.Scatter(x=spread.index,
                        y=spread,
                        mode='lines',
                        marker={'color':'rgb(189,189,189)',
                                'size':3},
                        name='Spread')
    fig4_2 = go.Scatter(x=spread.index,
                        y=data_mean,
                        mode='lines',
                        name='Spread Mean')
    fig4_3 = go.Scatter(x=spread.index,
                        y=data_upper_level,
                        mode='lines',
                        name='Upper Level')
    fig4_4 = go.Scatter(x=spread.index,
                        y=data_lower_level,
                        mode='lines',
                        name='Lower Level')
    layout4 = go.Layout(title='{}'.format(result_stationary),
                        yaxis={'tickformat':','})
    fig4 = go.Figure(data=[fig4_1,fig4_2,fig4_3,fig4_4],layout=layout4)
    fig4.update_layout(template='plotly_dark')

    return fig1,fig2,fig3,fig4

if __name__ == '__main__':
    app.run_server()