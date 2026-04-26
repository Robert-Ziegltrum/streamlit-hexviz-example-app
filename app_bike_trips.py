import streamlit as st
import streamlit_hexviz as shv
import pandas as pd


st.write("""# Biek trips London Example App""")

st.write("""This is a simple H3 viz app.
         The data set is from [Kaggle Data Sets](https://www.kaggle.com/datasets/prashantbrl/london-open-data-bike-and-mobility). 
         """
         )


@st.cache_data
def load_data():
    return pd.read_csv('data/bike_trips.csv')


df = load_data()

shv.h3_map(df, lat="start_lat", lon="start_long",
           resolution=3, use_sidebar_controls=True)

st.write("Tools shows the usage of the hexviz app for a geospatial data set")
st.write("""Guidance:
         - change resolutions to see different granularities
         - change color schemes
         - Transformation allows switching between different options: linear, log, quantil
         - enable 3d
         """)
# ---------footer-----------
st.divider()
st.markdown(
    "**streamlit-hexviz** · "
    "[GitHub](https://github.com/Robert-Ziegltrum/streamlit-hexviz) · "
    "[Kaggle Data Sets](https://www.kaggle.com/datasets/prashantbrl/london-open-data-bike-and-mobility)"

)
