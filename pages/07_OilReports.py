import streamlit as st

from helpers.ReportsWriter import oil_reporting

st.set_page_config(page_title="Data Reports (Oil)",
                   layout="wide")
st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Oil")

oil_report = oil_reporting()
with open("reports/Oil_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download oil report (HTML)",
        data=file,
        file_name="Oil_Reports.html",
        mime='text/html'
    )
