class LibraryLoader:
    '''
    StockAnalyzer에 필요한 라이브러리를 로드하는 클래스

    - 딕셔너리로 반환되어, 인덱싱을 이용해서 사용할 것
    - 딕셔너리를 반환하는 함수 이름 : `get_libs()`
    - pandas, numpy, FinanceDataReader, request, json, os, datetime, plotly 사용
    '''
    import pandas as pd
    import numpy as np
    import FinanceDataReader as fdr
    import requests
    import json
    import os
    import datetime
    import plotly.graph_objects as go
    from plotly import subplots

    @classmethod
    def get_libs(cls):
        """필요한 라이브러리를 딕셔너리로 반환"""
        return {
            "pd": cls.pd,
            "np": cls.np,
            "fdr": cls.fdr,
            "requests": cls.requests,
            "json": cls.json,
            "os": cls.os,
            "datetime": cls.datetime,
            "go": cls.go,
            "subplots": cls.subplots
        }

class StockAnalyzer:

    '''
    원하는 종목의 이름을 넣어주면, 주식가격, DrawDown, MACD, RSI, Volume을 그려주는 클래스

    - 주식 이름(한글로), 시작일자, 끝일자 
    - stock_data_reader()
    - calculate_mdd()
    - macd_oscillator()
    - rsi()
    - plot_analysis()
    '''
    def __init__(self, stock_name, start_date=None, end_date=None):
        self.libs = LibraryLoader.get_libs()  # 라이브러리 불러오기
        self.stock_name = stock_name
        self.start_date = start_date
        self.end_date = end_date
        self.df = self.stock_data_reader()

    def stock_listing(self):
        params ={
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT01901',
            'locale': 'ko_KR',
            'mktId': 'ALL',
            'share': '1',
            'csvxls_isNo': 'false'
        }
        
        #요청시 헤더 정보
        headers = {
            'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201',
            'Upgrade-Insecure-Requests': '1', 
            'User-Agent': 'Mozilla/5.0'
        }
        
        r = self.libs["requests"].post('http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd', params, headers=headers)
        jo = self.libs["json"].loads(r.text)
        df = self.libs["pd"].json_normalize(jo, 'OutBlock_1')
        df_info = df[['ISU_SRT_CD', 'ISU_ABBRV']]
        df_info.columns = ['Symbol', 'Name']
        return df_info
    
    def stock_data_reader(self):
        today_year = self.libs["datetime"].datetime.today().year
        today_month = self.libs["datetime"].datetime.today().month
        today_day = self.libs["datetime"].datetime.today().day
    
        # 2. KRX 종목 DataFrame 존재 여부 확인
        if self.libs["os"].path.isfile("krx_df_{}_{}_{}.csv".format(today_year, today_month, today_day)):
            krx_df = self.libs["pd"].read_csv("krx_df_{}_{}_{}.csv".format(today_year, today_month, today_day), index_col = 0)
        else:
            krx_df = self.stock_listing()
            krx_df.to_csv("krx_df_{}_{}_{}.csv".format(today_year, today_month, today_day))
        
        # 3. 종목 코드 찾기
        if self.stock_name in krx_df['Name'].values:
            symbol = krx_df[krx_df['Name'] == self.stock_name]['Symbol'].values[0]
        else:
            print("There is no name in KRX")
            raise "Threr is no name in KRX" # 함수가 중간에 멈추고 -> error 발생
        
        # 찾은 심볼을 가지고 -> 시작, 끝 날자의 상장 주식 정보를 반환함 !
        stock_df = self.libs["fdr"].DataReader(symbol, self.start_date, self.end_date)

        return stock_df
        
    def calculate_mdd(self):
        
        df = self.df[['Close']].copy()
        df['Return'] = df['Close'].pct_change().fillna(0)
        df['CumReturn'] = (1 + df['Return']).cumprod()
        df['MaxCumReturn'] = df['CumReturn'].cummax()
        df['DrawDown'] = (df['CumReturn'] / df['MaxCumReturn']) - 1
        
        mdd = df['DrawDown'].min()
        max_close_value = df['Close'].max()
        min_close_value = df['Close'].min()
        
        df_max_close = df[df['DrawDown'] == 0].copy()
        df_max_close.loc[df.index[-1]] = 0
        period = df_max_close.index[1:] - df_max_close.index[:-1]
        mdd_days = period.days
        max_period = mdd_days.max()
        max_period_idx = mdd_days.argmax()
        
        return df, [max_close_value, min_close_value, round(mdd * 100, 2), df_max_close.index[:-1][max_period_idx].date(), df_max_close.index[1:][max_period_idx].date(), max_period]
    
    def macd_oscillator(self, short_N=9, long_N=26, signal_N=13):
        '''
        단기이동평균(기본값) : 9일
        장기이동평균(기본값) : 26일
        시그널(기본값) : 13일일
        '''

        df = self.df[['Close']].copy()
        df['Short'] = df['Close'].ewm(span=short_N, adjust=False).mean()
        df['Long'] = df['Close'].ewm(span=long_N, adjust=False).mean()
        df['MACD'] = df['Short'] - df['Long']
        df['Signal'] = df['MACD'].ewm(span=signal_N, adjust=False).mean()
        df['MACD Oscillator'] = df['MACD'] - df['Signal']
        return df[['MACD', 'Signal', 'MACD Oscillator']]
    
    def rsi(self, rsi_period=14):
        '''
        rsi이동평균(기본값) : 14일
        현재 함수는 이동평균 : rolling(window=14)를 사용 중
        - 추후 지수이동평균으로 바꿀 
        '''
        df = self.df[['Close']].copy()
        df['Change'] = df['Close'].diff()
        df['Gain'] = self.libs["np"].where(df['Change'] >= 0, df['Change'], 0)
        df['Loss'] = self.libs["np"].where(df['Change'] < 0, -df['Change'], 0)
        df['avgGain'] = df['Gain'].rolling(window=rsi_period).mean()
        df['avgLoss'] = df['Loss'].rolling(window=rsi_period).mean()
        df['RS'] = df['avgGain'] / df['avgLoss']
        df['RSI'] = 100 - (100 / (1 + df['RS']))
        return df[['RSI']]
    
    def plot_analysis(self, short_N=9, long_N=26, signal_N=13, rsi_period=14):


        df_dd, stock_info = self.calculate_mdd()
        df_macd = self.macd_oscillator(short_N, long_N, signal_N)
        df_rsi = self.rsi(rsi_period)

        candlestick = self.libs["go"].Candlestick(x = self.df.index, open = self.df['Open'], high = self.df['High'], low = self.df['Low'], close = self.df['Close'], name = 'Candle Stick')
        dd = self.libs["go"].Scatter(x= df_dd.index, y = df_dd['DrawDown']*100, name = "Draw Down", fill="tozeroy")
        macd = self.libs["go"].Scatter(x=self.df.index, y=df_macd["MACD"], name="MACD")
        signal = self.libs["go"].Scatter(x=self.df.index, y=df_macd["Signal"], name="signal")
        oscillator = self.libs["go"].Bar(x=self.df.index, y=df_macd["MACD Oscillator"], name="oscillator")
        rsi = self.libs["go"].Scatter(x=df_rsi.index, y=df_rsi['RSI'], name="RSI")
        volume = self.libs["go"].Bar(x=self.df.index, y=self.df["Volume"], name="Volume", marker = dict(color='green'))
        fig = self.libs["subplots"].make_subplots(rows=5, cols=1,vertical_spacing = 0.01, shared_xaxes = True,
                                subplot_titles = ('<b>{}</b>'.format(self.stock_name),
                                                '<b>Draw Down</b>',
                                                '<b>MACD</b>',
                                                '<b>RSI</b>',
                                                '<b>Volume</b>'))
        
        
        fig.append_trace(candlestick, 1, 1)
        fig.append_trace(dd, 2, 1)
        fig.append_trace(macd, 3, 1)
        fig.append_trace(signal, 3, 1)
        fig.append_trace(oscillator, 3, 1)
        fig.append_trace(rsi, 4, 1)
        fig.add_trace(self.libs["go"].Scatter(x=df_rsi.index, y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*30,line=dict(color='red',dash='dash'),name='Low bound'),row=4,col=1)
        fig.add_trace(self.libs["go"].Scatter(x=df_rsi.index, y=(df_rsi['RSI']/df_rsi['RSI']).fillna(1)*70,line=dict(color='red',dash='dash'),name='High bound'),row=4,col=1)
        fig.append_trace(volume, 5, 1)
        fig.update_xaxes(rangeslider_visible=False)
        fig.update_layout(width = 1000, height = 1300)
        fig.update_layout(legend_title_text = "Content",
                    title = '{}, Max : {}, Min : {}, MDD : {}%, Period : {} ~ {}'.format(self.stock_name, stock_info[0], stock_info[1], stock_info[2], stock_info[3], stock_info[4])
                    )
        fig.update_yaxes(tickformat = ',')
        fig.show()
