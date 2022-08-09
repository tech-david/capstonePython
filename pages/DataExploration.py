import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from helpers.DataframeVIsuals import gas_raw_dataframe, elec_raw_dataframe, oil_raw_dataframe
from helpers.PlotVisuals import gas_raw_plot, elec_raw_plot, oil_raw_plot

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









# Creating reports, dropping date and day, as API recreates Date
# Dropping day as it creates incorrect correlation statistics
natural_gas_profile = ProfileReport(df_gas_data_fill_na.drop(columns=['Date', 'Day']),
                                    title="Natural Gas Reports",
                                    dataset={
                                        "description": "Reports of cleaned natural gas dataset"
                                    },
                                    variables={
                                        "descriptions": {
                                            "Natural Gas Price, Wellhead": "Price from source",
                                            "Natural Gas Price, Citygate": "Point of distribution",
                                            "Natural Gas Price, Delivered to Consumers, Residential": "Average price "
                                                                                                      "paid for by "
                                                                                                      "residential "
                                                                                                      "users ",
                                            "Natural Gas Price, Delivered to Consumers, Commercial": "Average price "
                                                                                                     "paid for by "
                                                                                                     "commercial "
                                                                                                     "users ",
                                            "Natural Gas Price, Delivered to Consumers, Industrial": "Average price "
                                                                                                     "paid for by "
                                                                                                     "industrial "
                                                                                                     "users ",
                                        }
                                    })

st.title("Reports of natural gas data after filling NA values")
natural_gas_report = st_profile_report(natural_gas_profile)
# Saving created report to folder
natural_gas_profile.to_file("reports/Natural_Gas_Reports.html")

with open("reports/Natural_Gas_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download natural gas report (HTML)",
        data=file,
        file_name="Natural_Gas_Reports.html",
        mime='text/html'
    )
