import streamlit as st
from helpers.ReportsView import cpi_reporting


st.set_page_config(page_title="Data Reports (CPI)",
                   layout="wide")
st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Consumer Price Index")

home_report = cpi_reporting()
with open("reports/CPI_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download home price report (HTML)",
        data=file,
        file_name="CPI_Reports.html",
        mime='text/html'
    )
