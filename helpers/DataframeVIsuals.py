from helpers.Cleaner import fill_electricity_na, fill_gas_na, fill_oil_na, fill_cpi_na
from helpers.GetRawData import get_gas_data, get_electricity_data, get_oil_data, get_cpi_data
import streamlit as st

from model.dataset.FullDataset import min_max_data
from model.dataset.TrainTestData import train_test_split_business_cycle
from model.features.PctChange import percent_change


def gas_raw_dataframe():
    df_gas_data = get_gas_data()
    # Default columns for natural gas view
    default_cols = ['Year',
                    'Month',
                    'Natural Gas Price, Wellhead',
                    'Natural Gas Price, Citygate',
                    'Natural Gas Price, Delivered to Consumers, Residential',
                    'Natural Gas Price, Delivered to Consumers, Commercial',
                    'Percentage of Electric Power Sector Consumption for Which Price Data Are Available']
    options = df_gas_data.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_gas_data[select_options])
    return filtered_df


def elec_raw_dataframe():
    df_electricity_data = get_electricity_data()
    # Default columns for electricity view
    default_cols = ['Year',
                    'Month',
                    'Average Retail Price of Electricity, Residential',
                    'Average Retail Price of Electricity, Commercial']
    options = df_electricity_data.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_electricity_data[select_options])
    return filtered_df


def oil_raw_dataframe():
    df_oil_data = get_oil_data()
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Regular Motor Gasoline, All Areas, Retail Price',
                    'On-Highway Diesel Fuel Price']
    options = df_oil_data.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_oil_data[select_options])
    return filtered_df


def cpi_raw_dataframe():
    df = get_cpi_data()
    default_cols = ['Year',
                    'Period',
                    'Bread',
                    'Chicken_Whole',
                    'Milk']
    options = df.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df[select_options])
    return filtered_df


# Dataframe for cleaned natural gas data
def post_processed_gas():
    df_gas_data_fill_na = fill_gas_na()
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Natural Gas Price, Delivered to Consumers, Residential',
                    'Natural Gas Price, Delivered to Consumers, Commercial'
                    ]
    options = df_gas_data_fill_na.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_gas_data_fill_na[select_options])
    return filtered_df


# Dataframe for cleaned electricity data
def post_processed_elec():
    df_electricity_data_fill_na = fill_electricity_na()
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Average Retail Price of Electricity, Residential',
                    'Average Retail Price of Electricity, Commercial'
                    ]
    options = df_electricity_data_fill_na.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_electricity_data_fill_na[select_options])
    return filtered_df


def post_processed_oil():
    df_oil_data_fill_na = fill_oil_na()
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Regular Motor Gasoline, All Areas, Retail Price'
                    ]
    options = df_oil_data_fill_na.columns.to_list()
    # Creating options to choose which columns to compare graphically
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_oil_data_fill_na[select_options])
    return filtered_df


def post_processed_cpi():
    df = fill_cpi_na()
    default_cols = ['Year',
                    'Bread',
                    'Chicken_Whole',
                    'Milk']
    options = df.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df[select_options])
    return filtered_df


def all_features():
    df = percent_change()
    default_cols = ['Natural Gas Price, Delivered to Consumers, Residential',
                    'Average Retail Price of Electricity, Residential',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Homes Average Sales Price']
    options = df.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df[select_options])
    return filtered_df


def std_features():
    df = min_max_data()
    default_cols = ['Natural Gas Price, Delivered to Consumers, Residential',
                    'Average Retail Price of Electricity, Residential',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Homes Average Sales Price']
    options = df.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df[select_options])
    return filtered_df


def split_dataframes():
    x_train, x_test, y_train, y_test = train_test_split_business_cycle()
    df_train = x_train.join(y_train, how='outer')
    df_test = x_test.join(y_test, how='outer')
    split_container = st.container()
    split_container.subheader("Train dataset")
    split_container.dataframe(df_train)
    split_container.subheader("Test dataset")
    split_container.dataframe(df_test)
    return split_container
