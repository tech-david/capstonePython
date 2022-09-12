import streamlit as st
st.set_page_config(page_title="Data Reports (Model ready data)",
                   layout="wide")
from helpers.ReportsView import model_data_reporting


st.title("Reports for data being used in model")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Model ready data")

home_report = model_data_reporting()
with open("reports/Model_Data_Report.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download model data report (HTML)",
        data=file,
        file_name="Model_Data_Report.html",
        mime='text/html'
    )
