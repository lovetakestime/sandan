import pandas as pd
import streamlit as st, numpy as np

from time import sleep


st.set_page_config(
    page_icon="🍭",
    page_title="연구자분석",
    layout="wide",
)

#페이지헤더, 서브헤더 제목설정
st.header("영남대학교 연구자 분석")
st.subheader("베타버전")

cols = st.columns((1,1,2))
cols[0].metric("10/11","15°C","2")
cols[0].metric("10/11","15°C","2")
cols[1].metric("11/12","17°C","-2")
cols[1].metric("11/12","17°C","-2")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

cols[2].line_chart(chart_data)  
