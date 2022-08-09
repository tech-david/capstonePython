from streamlit_pandas_profiling import st_profile_report
import streamlit as st

from helpers.ReportBuilder import create_gas_profile, create_elec_profile, create_oil_profile


# Saving created report to folder
def gas_profile():
    natural_gas_profile = create_gas_profile()
    natural_gas_profile.to_file("reports/Natural_Gas_Reports.html")
    return natural_gas_profile


def elec_profile():
    electric_profile = create_elec_profile()
    electric_profile.to_file("reports/Electricity_Reports.html")
    return electric_profile


def fuel_profile():
    oil_profile = create_oil_profile()
    oil_profile.to_file("reports/Oil_Reports.html")
    return oil_profile


# Populating data into page
def gas_reporting():
    with st.spinner(text="Creating natural gas reports"):
        natural_gas_profile = gas_profile()
        natural_gas_report = st_profile_report(natural_gas_profile)
        return natural_gas_report


def elec_reporting():
    with st.spinner(text="Creating electricity reports"):
        electric_profile = elec_profile()
        electric_report = st_profile_report(electric_profile)
        return electric_report


def oil_reporting():
    with st.spinner(text="Creating oil reports"):
        oil_profile = fuel_profile()
        oil_report = st_profile_report(oil_profile)
        return oil_report
