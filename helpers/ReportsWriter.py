from helpers.ReportBuilder import create_gas_profile, create_elec_profile, create_oil_profile, create_home_profile, \
    create_features_profile


# Saving created reports to folder as an HTML file
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


def house_profile():
    home_profile = create_home_profile()
    home_profile.to_file("reports/House_Reports.html")
    return home_profile


def features_profile():
    feature_profile = create_features_profile()
    feature_profile.to_file("reports/Features_Report.html")
    return feature_profile
