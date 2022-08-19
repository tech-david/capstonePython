import streamlit as st
from helpers.DataframeVIsuals import gas_raw_dataframe, elec_raw_dataframe, oil_raw_dataframe, cpi_raw_dataframe
from helpers.GetRawData import get_raw_house_data, get_recession_data
from helpers.PlotVisuals import gas_raw_plot, elec_raw_plot, oil_raw_plot, house_raw_plot, recession_raw_plot, \
    cpi_raw_plot

st.set_page_config(page_title="Data Exploration",
                   layout="wide")
st.title("Economic Recessions Using Commodities")
st.markdown("Predicting recessions using common consumer commodities")
st.write(
    """Preloaded data view.  To come: Uploading own data.
    """
)

st.header("Commodities Include:")
st.markdown("> Natural gas, oil products, electricity, housing, CPI of common household goods.")
st.sidebar.header("Preloaded data exploration")

st.header("Natural Gas Prices Jan 1976 - Dec 2021")

st.subheader("Natural Gas Price Data")
gas_raw_dataframe()

st.subheader("Natural Gas Price Graph")
gas_raw_plot()

st.header("Electricity Prices Jan 1976 - Dec 2021")

st.subheader("Electricity Price Data")
elec_raw_dataframe()

st.subheader("Electricity Price Graph")
elec_raw_plot()

st.header("Oil Product Prices Jan 1976 - Dec 2021")

st.subheader("Oil Price Data")
oil_raw_dataframe()

st.subheader("Oil/Fuel Price Graph")
oil_raw_plot()

st.header("Home Prices (Avg & Median) 1973-2021")
st.subheader("Home Price Data")
st.dataframe(get_raw_house_data())

st.subheader("Home Price Graph")
house_raw_plot()

st.header("NBER Indicated Recessions 1940-2021")
st.subheader("Recession Data")
st.markdown("> 0 indicates no recession, 1 indicates recession")
st.dataframe(get_recession_data())

st.subheader("Recession Graph")
recession_raw_plot()

st.header("CPI for various goods 1976-2022")
st.markdown(">CPI data is in terms of 1 month change")
st.subheader("CPI Data")
cpi_raw_dataframe()
st.subheader("CPI Graph")
cpi_raw_plot()
