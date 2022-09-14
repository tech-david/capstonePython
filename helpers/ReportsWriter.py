from helpers.ReportBuilder import create_gas_profile, create_elec_profile, create_oil_profile, create_home_profile, \
    create_features_profile, create_model_data_profile, create_cpi_profile


# Saving created reports to folder as an HTML file

# AWS local path
PATH = '/home/ec2-user/capstonePython/reports/'


def gas_profile():
    natural_gas_profile = create_gas_profile()
    natural_gas_profile.to_file(PATH+"Natural_Gas_Reports.html")
    return natural_gas_profile


def elec_profile():
    electric_profile = create_elec_profile()
    electric_profile.to_file(PATH+"Electricity_Reports.html")
    return electric_profile


def fuel_profile():
    oil_profile = create_oil_profile()
    oil_profile.to_file(PATH+"Oil_Reports.html")
    return oil_profile


def house_profile():
    home_profile = create_home_profile()
    home_profile.to_file(PATH+"House_Reports.html")
    return home_profile


def write_cpi_profile():
    profile = create_cpi_profile()
    profile.to_file(PATH+"CPI_Reports.html")
    return profile


def features_profile():
    feature_profile = create_features_profile()
    feature_profile.to_file(PATH+"Features_Report.html")
    return feature_profile


def model_data_profile():
    feature_profile = create_model_data_profile()
    feature_profile.to_file(PATH+"Model_Data_Report.html")
    return feature_profile
