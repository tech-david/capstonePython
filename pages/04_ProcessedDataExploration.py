import streamlit as st
st.set_page_config(page_title="Data Exploration After Cleaning",
                   layout="wide")
from helpers.Cleaner import resample_house
from helpers.DataframeVIsuals import post_processed_gas, post_processed_elec, post_processed_oil, post_processed_cpi
from helpers.GetRawData import get_recession_data
from helpers.PlotVisuals import gas_clean_plot, elec_clean_plot, oil_clean_plot, house_clean_plot, recession_raw_plot, \
    cpi_clean_plot


st.title("Economic Recessions Using Commodities")
st.markdown("Predicting recessions using common consumer commodities")
st.write(
    """Preloaded cleaned data view
    """
)

st.sidebar.header("Cleaned data exploration")
st.header("Exploration Post Processed")
st.markdown("> Including removal of columns, and filling null values using interpolation")

st.header("Natural Gas Prices Jan 1976 - Dec 2021")
st.subheader("Natural Gas (Cleaned) Data")

post_processed_gas()
st.subheader("Natural Gas (Cleaned) Price Graph")
gas_clean_plot()

st.header("Electricity Prices Jan 1976 - Dec 2021")
st.subheader("Electricity (Cleaned) Data")
post_processed_elec()

st.subheader("Electricity (Cleaned) Price Graph")
elec_clean_plot()

st.header("Oil Product Prices Jan 1976 - Dec 2021")
st.subheader("Oil (Cleaned) Data")
post_processed_oil()

st.subheader("Oil (Cleaned) Price Graph")
oil_clean_plot()

st.header("Home Prices (Avg & Median) 1973-2021")
st.subheader("Home Price Data")
st.dataframe(resample_house().style.format("{:.2f}"))

st.subheader("Home Price Graph")
house_clean_plot()

st.header("CPI for Common Groceries 1961-2022")
st.subheader("CPI data")
post_processed_cpi()
st.subheader("CPI (Cleaned) Graph")
cpi_clean_plot()

st.header("NBER Indicated Recessions 1940-2021")
st.subheader("Recession Data")
st.markdown("> 0 indicates no recession, 1 indicates recession")
st.dataframe(get_recession_data())

st.subheader("Recession Graph")
recession_raw_plot()
