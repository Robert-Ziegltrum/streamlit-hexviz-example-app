import streamlit as st
import streamlit_hexviz as shv
import pandas as pd


st.write("""# Truck Parking Locations Europe Example App""")

st.write("""This is a simple H3 viz app.
         The data set is from [Kaggle Data Sets](https://www.kaggle.com/datasets/mexwell/european-truck-parking-locations). 
         """
         )


@st.cache_data
def load_data():
    return pd.read_csv('data/truck_parking_europe.csv', delimiter=";")


df = load_data()

shv.h3_map(df, lat="lat", lon="lon",
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
    "[Kaggle Data Sets](https://www.kaggle.com/datasets/mexwell/european-truck-parking-locations)"

)
