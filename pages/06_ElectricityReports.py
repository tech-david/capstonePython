import streamlit as st

from helpers.ReportsView import elec_reporting

st.set_page_config(page_title="Data Reports (Electricity)",
                   layout="wide")
st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Electricity")

electric_report = elec_reporting()
with open("reports/Electricity_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download electricity report (HTML)",
        data=file,
        file_name="Electricity_Reports.html",
        mime='text/html'
    )
