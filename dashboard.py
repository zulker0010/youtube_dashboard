import numpy as np 
import pandas as pd
import streamlit as st
import openpyxl
import altair as alt
from preprocessor_script import df, df_selected_country

st.set_page_config(
    page_title='YouTube Dashboard',
    page_icon='📈',
    layout='wide'
)

data_source = pd.read_excel(r"F:\Data Analytics\youtube_dashboard\Global_YouTube_Statistics.xlsx")

top_ranked_channels = data_source.iloc[:,:3]
print(top_ranked_channels)


st.title(':jetblack[YouTube Dashboard📈]')

col = st.columns((2,4,5), gap = 'large')



#select a country
with col[0]:
    country_list = list(df.Country.unique())[::-1]
    selected_country = st.selectbox('Select a country', country_list)
    df_selected_country = df[df.Country == selected_country]

    

with col[2]:
    st.markdown('Top 10 YouTube Channels')
    
    st.dataframe(
        top_ranked_channels, 
        hide_index = True,
        column_config={
            'rank':st.column_config.TextColumn(
                'rank'
                ),
            'Youtuber': st.column_config.TextColumn(
                'Youtuber'
                ),
            'subscribers': st.column_config.ProgressColumn(
                'subscribers',
                 min_value=0.0,
                 max_value=max(top_ranked_channels['subscribers'] )
                )
        }
            )
    

