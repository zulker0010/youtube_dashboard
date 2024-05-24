import numpy as np 
import pandas as pd
import streamlit as st
import openpyxl


data_source = pd.read_excel(r"F:\Data Analytics\youtube_dashboard\Global_YouTube_Statistics.xlsx")

top_ranked_channels = data_source.iloc[:,:3]
print(top_ranked_channels)

st.title(':jetblack[YouTube Dashboard📈]')

col = st.columns((1,5,4), gap = 'small')

with col[2]:
    st.markdown('Top 10 YouTube Channels')
    
    st.dataframe(
        top_ranked_channels, 
        hide_index = True,
    )


