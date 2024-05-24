import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import openpyxl
import plotly_express as plx

data_source = pd.read_excel(r"F:\Data Analytics\youtube_dashboard\Global_YouTube_Statistics.xlsx")
