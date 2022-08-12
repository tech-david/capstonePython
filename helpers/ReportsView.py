import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from helpers.ReportsWriter import gas_profile, elec_profile, fuel_profile, house_profile, features_profile


# Populating data into page using spinner to indicate loading
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


def home_reporting():
    with st.spinner(text="Creating home reports"):
        home_profile = house_profile()
        home_report = st_profile_report(home_profile)
        return home_report


def feature_reporting():
    with st.spinner(text='Creating feature reports'):
        feature_profile = features_profile()
        feature_report = st_profile_report(feature_profile)
        return feature_report
