from model.features.FeaturesAggregator import get_all_features
import streamlit as st


@st.cache
def percent_change():
    df = get_all_features()
    df = df.pct_change(periods=1,
                       fill_method='bfill',
                       freq='MS')
    return df
