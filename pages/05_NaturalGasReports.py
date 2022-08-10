import streamlit as st

from helpers.ReportsWriter import gas_reporting

st.set_page_config(page_title="Data Reports (Natural Gas)",
                   layout="wide")
st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Natural Gas")

natural_gas_report = gas_reporting()
with open("reports/Natural_Gas_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download natural gas report (HTML)",
        data=file,
        file_name="Natural_Gas_Reports.html",
        mime='text/html'
    )
