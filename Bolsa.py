import yfinance as yf
import pandas as pd
from datetime import datetime
import streamlit as st
def normal(param: list):
    if type(param) != list:
      param = list(param)

    dicto = {'id': [], 'contentType': [], 'title': [], 'description': [], 'summary': [], 'pubDate': [], 'isHosted': [], 'bypassModal': [], 'previewUrl': [], 'thumbnail': [], 'provider': [], 'canonicalUrl': [], 'clickThroughUrl': [], 'metadata': [], 'finance': [], 'storyline': []}

    for varredura in range(len(param)):
      for chave in dicto.keys():
        dicto[chave].append(param[varredura][chave])

    return pd.DataFrame(dicto)
st.markdown('# Analisando empresas')
st.text_input('Ticker Code:', key = 'tickercode', value= 'GOOG')
st.markdown(f'## Últimas notícias da {st.session_state.tickercode}:')
ticker = st.session_state.tickercode #Da empresa do Google
data =  yf.Ticker(ticker)
data_news=normal(pd.DataFrame(data.news)['content'])
data_news2 = data_news[['title', 'summary', 'canonicalUrl']]
st.dataframe(data_news2)

end_date = datetime.now().strftime('%Y-%m-%d')
data_hist = data.history(period= 'max', start= '2020-03-16', end= end_date, interval= '5d')
data_hist = data_hist.reset_index()

st.markdown('# Construa seu gráfico:')

ey = st.selectbox('Eixo Y:', data_hist.columns)
ex = st.selectbox('Eixo X:', data_hist.columns)
st.markdown(f'## Gráfico {ey} x {ex}:')
st.line_chart(data_hist, x = f'{ex}',y = f'{ey}')