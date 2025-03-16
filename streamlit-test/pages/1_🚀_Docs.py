import pandas as pd
import streamlit as st, numpy as np
import plotly.express as px
from time import sleep


@st.cache_data
def load_excel(file):
    return pd.read_excel(file,engine='openpyxl')

@st.cache_data
def load_csv(file):
    return pd.read_csv(file)


st.set_page_config(
    page_icon="🍭",
    page_title="연구자분석",
    layout="wide",
)

#페이지헤더, 서브헤더 제목설정
st.subheader("도큐먼트")

if st.button("클릭 보기"):
    st.text("안녕하세요")


file = st.file_uploader("파일을 업로드 해주세요", type=('csv','xlsx','xls'))
                        
if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = load_csv(file)
        
    elif 'xls' in ext:
        df = load_excel(file)
    
    st.write("데이터 미리보기")
    st.dataframe(df.head(10))
    df['과제년도'] = df['과제년도'].astype(int)
    소속대학리스트 = np.sort(df['소속대학'].dropna().unique())
    selected_value = st.selectbox("소속대학 (가나다 순)", 소속대학리스트)
    

    소속대학별간접비 = df.groupby(['소속대학','과제년도'])["간접비금액"].sum()
    선택대학간접비 = 소속대학별간접비.loc[selected_value].reset_index()
    
    

    fig = px.line(선택대학간접비, x="과제년도", y="간접비금액", 
                      title=f"📈 {selected_value}의 연도별 간접비(원) 합계 변화",
                      markers=True)
    fig.update_traces(line=dict(width=2))  # 선 굵기 조정
    st.plotly_chart(fig)