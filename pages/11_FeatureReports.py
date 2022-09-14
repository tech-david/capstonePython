import streamlit as st
st.set_page_config(page_title="Data Reports (All Features)",
                   layout="wide")
from helpers.ReportsView import feature_reporting


st.title("Reports for datasets after cleaning")
st.markdown("> Resource intensive page, please allow time for processing")
st.markdown("> Can download once process is completed")
st.markdown("> Download button located at end of report")
st.subheader("Features in one dataset")

home_report = feature_reporting()
with open("/home/ec2-user/capstonePython/reports/Features_Report.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download feature report (HTML)",
        data=file,
        file_name="Features_Report.html",
        mime='text/html'
    )
