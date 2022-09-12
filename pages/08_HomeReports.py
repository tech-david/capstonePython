import streamlit as st
st.set_page_config(page_title="Data Reports (Home Prices)",
                   layout="wide")
from helpers.ReportsView import home_reporting


st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Home Prices")

home_report = home_reporting()
with open("reports/House_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download home price report (HTML)",
        data=file,
        file_name="Home_Price_Reports.html",
        mime='text/html'
    )
