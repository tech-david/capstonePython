import streamlit as st

from helpers.DataframeVIsuals import std_features
from helpers.PlotVisuals import std_plot, std_corr_map, std_corr_matrix, std_corr_map_after
from model.dataset.FullDataset import describe_std_data
from model.features.Preparation import drop_high_vif
from helpers.Metrics import calculate_vif, calculate_vif_after

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
std_corr_map()
std_corr_matrix()
st.subheader("Variance Inflation Factor")
calculate_vif()
st.markdown(">Various features show high variance correlation, those features will be dropped")
st.subheader("Highly correlated features dropped")
st.write(drop_high_vif())
st.subheader("VIF after")
calculate_vif_after()
st.subheader("Correlation heatmap after drop")
std_corr_map_after()

