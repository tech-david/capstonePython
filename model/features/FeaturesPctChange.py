from model.features.FeaturesAggregator import get_all_features
import streamlit as st


# Calculating percentage difference between each timestamps (row index)
@st.cache
def percent_change():
    df = get_all_features()
    df = df.pct_change(periods=1,
                       fill_method='bfill',
                       freq='MS')  # MS - Month start
    return df
