import streamlit as st
st.set_page_config(page_title="Percentages Standardized",
                   layout='wide')

from helpers.DataframeVIsuals import std_features
from helpers.PlotVisuals import std_plot, std_corr_map, std_corr_matrix, std_corr_map_after
from model.dataset.FullDataset import describe_std_data
from model.features.Preparation import get_best
from helpers.Metrics import calculate_vif, calculate_vif_after
from model.regression.LogisticModel import best_features


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
st.markdown(">Various features show high variance correlation")
st.subheader("Best features")
st.markdown(">Checking for best features in regression model")
best_features()
st.subheader("Best features selected")
st.write(get_best())
st.subheader("VIF after")
calculate_vif_after()
st.subheader("Correlation heatmap after drop")
std_corr_map_after()
