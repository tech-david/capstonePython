from helpers.Cleaner import fill_gas_na, fill_electricity_na, fill_oil_na, resample_house, fill_cpi_na
from pandas_profiling import ProfileReport

from model.features.Preparation import get_best
from model.features.PctChange import percent_change


# Creating reports, dropping date and day, as API recreates Date
def create_gas_profile():
    df = fill_gas_na()

    # Dropping day as it creates incorrect correlation statistics
    natural_gas_profile = ProfileReport(df.drop(columns=['Date', 'Day', 'Year', 'Month']),
                                        title="Natural Gas Reports",
                                        minimal=True,
                                        dataset={
                                            "description": "Reports of cleaned natural gas dataset"
                                        },
                                        variables={
                                            "descriptions": {
                                                "Natural Gas Price, Wellhead": "Price from source",
                                                "Natural Gas Price, Citygate": "Point of distribution",
                                                "Natural Gas Price, Delivered to Consumers, Residential": "Average "
                                                                                                          "price "
                                                                                                          "paid for by "
                                                                                                          "residential "
                                                                                                          "users ",
                                                "Natural Gas Price, Delivered to Consumers, Commercial": "Average "
                                                                                                         "price "
                                                                                                         "paid for by "
                                                                                                         "commercial "
                                                                                                         "users ",
                                                "Natural Gas Price, Delivered to Consumers, Industrial": "Average "
                                                                                                         "price "
                                                                                                         "paid for by "
                                                                                                         "industrial "
                                                                                                         "users "

                                            }
                                        })
    return natural_gas_profile


def create_elec_profile():
    df = fill_electricity_na()
    electricity_profile = ProfileReport(df.drop(columns=['Date', 'Day', 'Year', 'Month']),
                                        title='Electricity Reports',
                                        minimal=True,
                                        dataset={
                                            "description": "Reports of cleaned electricity dataset"
                                        },
                                        variables={
                                            "descriptions": {
                                                "Average Retail Price of Electricity, Residential": "Price paid by "
                                                                                                    "residential "
                                                                                                    "homes",
                                                "Average Retail Price of Electricity, Commercial": "Price paid by "
                                                                                                   "commercial "
                                                                                                   "entities",
                                                "Average Retail Price of Electricity, Industrial": "Price paid by "
                                                                                                   "industrial "
                                                                                                   "companies",
                                                "Average Retail Price of Electricity, Transportation": "Price paid by "
                                                                                                       "electrical "
                                                                                                       "transportation "
                                                                                                       "users",
                                                "Average Retail Price of Electricity, Total": "Cumulative mean of all "
                                                                                              "categories"
                                            }
                                        })
    return electricity_profile


def create_oil_profile():
    df = fill_oil_na()
    oil_profile = ProfileReport(df.drop(columns=['Date', 'Day', 'Year', 'Month']),
                                title="Oil Reports",
                                minimal=True,
                                dataset={
                                    "description": "Reports of cleaned oil dataset"
                                },
                                variables={
                                    "descriptions": {
                                        "Leaded Regular Gasoline, U.S. City Average Retail Price": "Price of leaded "
                                                                                                   "fuel, "
                                                                                                   "0 when "
                                                                                                   "discontinued",
                                        "Unleaded Regular Gasoline, U.S. City Average Retail Price": "Price of "
                                                                                                     "unleaded fuel, "
                                                                                                     "0 when leaded "
                                                                                                     "was used",
                                        "Unleaded Premium Gasoline, U.S. City Average Retail Price": "Price of "
                                                                                                     "premium "
                                                                                                     "unleaded fuel",
                                        "All Grades of Gasoline, U.S. City Average Retail Price": "Cumulative of all "
                                                                                                  "grades of gasoline",
                                        "Regular Motor Gasoline, Conventional Gasoline Areas, Retail Price": "Price "
                                                                                                             "of "
                                                                                                             "fuel, "
                                                                                                             "non-"
                                                                                                             "blended",
                                        "Regular Motor Gasoline, Reformulated Gasoline Areas, Retail Price": "Price "
                                                                                                             "of "
                                                                                                             "fuel, "
                                                                                                             "blended",
                                        "Regular Motor Gasoline, All Areas, Retail Price": "Cumulative mean of all "
                                                                                           "categories",
                                        "On-Highway Diesel Fuel Price": "Price for diesel fuel"
                                    }
                                })
    return oil_profile


def create_home_profile():
    df = resample_house()
    home_profile = ProfileReport(df,
                                 title='Home Price Reports',
                                 minimal=True,
                                 dataset={
                                     "description": "Reports of average and median home prices in US"
                                 },
                                 variables={
                                     "descriptions": {
                                         "Average Sales Price": "Average price of homes sold in $",
                                         "Median Sales Price": "Median price of homes sold in $"
                                     }
                                 })
    return home_profile


def create_cpi_profile():
    df = fill_cpi_na()
    cpi_profile = ProfileReport(df,
                                title='CPI reports',
                                minimal=True,
                                dataset={
                                    "description": "Reports of monthly change of CPI for commodities"
                                })
    return cpi_profile


def create_features_profile():
    df = percent_change()
    # Setting minimal to True due to avoid memory leak
    feature_profile = ProfileReport(df,
                                    minimal=True,
                                    title='Cumulative Report of all Features',
                                    dataset={
                                        "description": "Reports of all features in one dataset"
                                    },
                                    variables={
                                        "descriptions": {
                                            "Natural Gas Price, Wellhead": "Price from source",
                                            "Natural Gas Price, Citygate": "Point of distribution",
                                            "Natural Gas Price, Delivered to Consumers, Residential": "Average "
                                                                                                      "price "
                                                                                                      "paid for by "
                                                                                                      "residential "
                                                                                                      "users ",
                                            "Natural Gas Price, Delivered to Consumers, Commercial": "Average "
                                                                                                     "price "
                                                                                                     "paid for by "
                                                                                                     "commercial "
                                                                                                     "users ",
                                            "Natural Gas Price, Delivered to Consumers, Industrial": "Average "
                                                                                                     "price "
                                                                                                     "paid for by "
                                                                                                     "industrial "
                                                                                                     "users ",
                                            "Average Retail Price of Electricity, Residential": "Price paid by "
                                                                                                "residential "
                                                                                                "homes",
                                            "Average Retail Price of Electricity, Commercial": "Price paid by "
                                                                                               "commercial "
                                                                                               "entities",
                                            "Average Retail Price of Electricity, Industrial": "Price paid by "
                                                                                               "industrial "
                                                                                               "companies",
                                            "Average Retail Price of Electricity, Transportation": "Price paid by "
                                                                                                   "electrical "
                                                                                                   "transportation "
                                                                                                   "users",
                                            "Average Retail Price of Electricity, Total": "Cumulative mean of all "
                                                                                          "categories",
                                            "Leaded Regular Gasoline, U.S. City Average Retail Price": "Price of "
                                                                                                       "leaded "
                                                                                                       "fuel, "
                                                                                                       "0 when "
                                                                                                       "discontinued",
                                            "Unleaded Regular Gasoline, U.S. City Average Retail Price": "Price of "
                                                                                                         "unleaded "
                                                                                                         "fuel, "
                                                                                                         "0 when "
                                                                                                         "leaded "
                                                                                                         "was used",
                                            "Unleaded Premium Gasoline, U.S. City Average Retail Price": "Price of "
                                                                                                         "premium "
                                                                                                         "unleaded fuel",
                                            "All Grades of Gasoline, U.S. City Average Retail Price": "Cumulative of "
                                                                                                      "all "
                                                                                                      "grades of "
                                                                                                      "gasoline",
                                            "Regular Motor Gasoline, Conventional Gasoline Areas, Retail Price": "Price "
                                                                                                                 "of "
                                                                                                                 "fuel, "
                                                                                                                 "non-"
                                                                                                                 "blended",
                                            "Regular Motor Gasoline, Reformulated Gasoline Areas, Retail Price": "Price "
                                                                                                                 "of "
                                                                                                                 "fuel, "
                                                                                                                 "blended",
                                            "Regular Motor Gasoline, All Areas, Retail Price": "Cumulative mean of all "
                                                                                               "categories",
                                            "On-Highway Diesel Fuel Price": "Price for diesel fuel",
                                            "Average Sales Price": "Average price of homes sold in $",
                                            "Median Sales Price": "Median price of homes sold in $"
                                        }
                                    })
    return feature_profile


def create_model_data_profile():
    df = get_best()
    feature_profile = ProfileReport(df,
                                    minimal=True,
                                    title="Model ready data",
                                    dataset={
                                        "description": "Data after feature prices changes have been calculated,"
                                                       " results standardized, and multicollinearity risk features"
                                                       " dropped"
                                    })
    return feature_profile
