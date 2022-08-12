import streamlit as st

from helpers.PlotVisuals import pct_change_plot
from model.features.FeaturesAggregator import get_all_features
from model.features.FeaturesPctChange import percent_change
st.set_page_config(page_title='Page for development of new features',
                   layout='wide')
st.dataframe(percent_change())
pct_change_plot()
