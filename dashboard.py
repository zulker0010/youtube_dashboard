import numpy as np 
import pandas as pd
import streamlit as st
import openpyxl
import altair as alt
from gauth_script import df
from preprocessor_script import most_viewed_channel, format_num, highest_earning_channel, most_popular_category

st.set_page_config(
    page_title='YouTube Dashboard',
    page_icon='📈',
    layout='wide'
)

top_ranked_channels = df.iloc[:,1:4]
print(top_ranked_channels)
st.title(':jetblack[YouTube Dashboard📈]')

col = st.columns((3,3,5), gap = 'large')

#select a country
with col[0]:
    country_list = list(df.Country.unique())[::-1]
    selected_country = st.selectbox('Select a country', country_list)
    df_selected_country = df[df.Country == selected_country]
    
    channel_name, view_count = most_viewed_channel(selected_country)
    max_earning_channel, highest_earning = highest_earning_channel(selected_country)
    category_name, sub_count = most_popular_category(selected_country)
    format_view_count = format_num(view_count)

with col[1]:
    with st.container(border=True): 
        st.metric(
            'Most viewed channel',  
            f'{channel_name}'
        )
        st.subheader(
            f'{format_view_count} views'
        )
        
    with st.container(border=True): 
        st.metric(
            label = 'Highest Earning Channel',
            value = f'{max_earning_channel}'       
        )
        st.subheader(
            f'${highest_earning}'
        )
    
    with st.container(border=True):
        st.metric(
            label = 'Most Popular Category',
            value = f'{category_name}'
        )
        st.subheader(
            f'{sub_count}'
        )

with col[2]:
    
    st.markdown('Top 10 YouTube Channels')
    
    st.dataframe(
        top_ranked_channels, 
        hide_index = True,
        column_config={
            'rank':st.column_config.TextColumn(
                'Rank'
                ),
            'Youtuber': st.column_config.TextColumn(
                'Youtuber'
                ),
            'subscribers': st.column_config.ProgressColumn(
                'Subscribers',
                format='',
                 min_value=0.0,
                 max_value=max(top_ranked_channels['subscribers'] )
                )
        }
            )
    

