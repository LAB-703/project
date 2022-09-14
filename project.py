import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px

chart = functools.partial(st.plotly_chart, use_container_width=True)
COMMON_ARGS = {
    "color": "symbol",
    "color_discrete_sequence": px.colors.sequential.Greens,
    "hover_data": [
        "account_name",
        "percent_of_account",
        "quantity",
        "total_gain_loss_dollar",
        "total_gain_loss_percent",
    ],
}

st.set_page_config(
        "Search Engine Dashboard",
        "📈",
        initial_sidebar_state="expanded",
        layout="wide",
    )


##################################################################
    st.sidebar.subheader("Search Engine")
    
    keyword = st.sidebar.text_input('keyword', '탈원전')
    st.write(keyword)
    st.sidebar.write('keyword is', keyword)

   
    accounts = ['naver_news','naver_cafe','naver_blog', 'daum_news','daum_cafe','daum_blog','youtube','tweeter','facebook','instagram']
    account_selections = st.sidebar.multiselect(
        "Select Accounts to View", options=accounts, default=accounts
    )

    st.subheader("Selected Account and Ticker Data")

    Start_date = st.sidebar.date_input(
     "Start date")
    st.sidebar.write('Start date is:', Start_date)
    
    End_date = st.sidebar.date_input(
     "End date")
    st.sidebar.write('End date is:', End_date)
    
##################################################################
    head="키워드 " +"탈원전"+"에 대한 검색결과는 다음과 같습니다."
    st.header(head)
