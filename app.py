from altair.vegalite.v4.schema.channels import Column

import pandas as pd

import streamlit as st

import plotly.express as px

from PIL import Image

import numpy as np

import altair as alt


from pandas_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title='Ninja Reviews')

st.header('Valve Software 2021')

st.subheader('Analytics based on the reviews of the game.')


# --- LOAD DATAFRAME

csv_file = 'reviews-1-115.csv'


# Weighted vote score

df1 = pd.read_csv(

    'https://game-reviews.s3.ap-south-1.amazonaws.com/reviews-1-115.csv')

st.header('**Top 10 Weighted vote score**')

result = df1.sort_values(['weighted_vote_score'], ascending=[0])

st.dataframe(result.head(10))


# Game percentage

# st.bar_chart(data=None, width=0, height=0, use_container_width=True)


if csv_file is not None:

    @st.cache
    def load_xlsx():

        xlsx = pd.read_csv(csv_file)

        return xlsx

    df = load_xlsx()

    pr = ProfileReport(df, explorative=True)

    st.header('**Input DataFrame**')

    st.write(df)

    st.write('---')

    st.header('**Pandas Profiling Report**')

    st_profile_report(pr)
