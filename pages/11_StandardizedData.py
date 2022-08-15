import streamlit as st

from helpers.DataframeVIsuals import std_features
from helpers.PlotVisuals import std_plot, std_box_plots
from model.dataset.FullDataset import describe_std_data

st.set_page_config(page_title="Percentages Standardized",
                   layout='wide')
st.header("Price changes standardized")
st.subheader("Price Change Data")
std_features()
st.subheader("Price Change Graphs")
std_plot()
st.subheader("Price change metrics")
describe_std_data()
st.subheader("Correlation of features")
std_box_plots()
