import streamlit as st

from helpers.DataframeVIsuals import split_dataframes
from helpers.PlotVisuals import split_plot

st.set_page_config(page_title="Train and Test Datasets",
                   layout="wide")
st.header("Data after splitting in accordance to typical business cycle")
split_dataframes()
st.subheader("Train/Test Graphs")
st.markdown(">Blue indicates training data, red indicates testing data")
split_plot()
