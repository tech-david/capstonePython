import streamlit as st
from helpers.DataframeVIsuals import all_features
from helpers.PlotVisuals import pct_change_plot

st.set_page_config(page_title="Percentage Difference",
                   layout='wide')
st.title("Price Percentage Increases")
st.markdown("Change in prices of commodities by percent")
st.markdown(">Monthly Change in prices")
st.sidebar.header("Prices Increase/Decrease")
st.subheader("Price Change Data")
all_features()
st.subheader("Price Change Graphs")
pct_change_plot()

