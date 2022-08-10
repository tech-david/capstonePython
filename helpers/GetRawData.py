import streamlit as st
import pandas as pd
import numpy as np


# Helper file to get raw data
# Using cache to save resources
@st.cache
def get_gas_data():
    df_gas_data = pd.read_csv("data/Table_9.10_Natural_Gas_Prices.csv",
                              header=[0],
                              skiprows=[1],
                              na_values="Not Available")
    # Convert prices to float
    ng_cols = df_gas_data.columns
    df_gas_data[ng_cols[1:]] = df_gas_data[ng_cols[1:]].apply(pd.to_numeric, errors='coerce')
    # Convert Month column into Year Month
    df_gas_data[['Year', 'Month']] = df_gas_data['Month'].str.split(' ', 1, expand=True)
    move_year_to_first = df_gas_data.pop('Year')
    df_gas_data.insert(0, 'Year', move_year_to_first)
    return df_gas_data


@st.cache
def get_electricity_data():
    df_electricity_data = pd.read_csv("data/Table_9.8_Average_Retail_Prices_of_Electricity.csv",
                                      header=[0],
                                      skiprows=[1],
                                      na_values="Not Available")
    elec_cols = df_electricity_data.columns
    # Convert prices to float
    df_electricity_data[elec_cols[1:]] = df_electricity_data[elec_cols[1:]].apply(pd.to_numeric, errors='coerce')
    # Convert Month column into Year Month
    df_electricity_data[['Year', 'Month']] = df_electricity_data['Month'].str.split(' ', 1, expand=True)
    move_year_to_first_elec = df_electricity_data.pop('Year')
    df_electricity_data.insert(0, 'Year', move_year_to_first_elec)
    return df_electricity_data


@st.cache
def get_oil_data():
    df_oil_data = pd.read_csv("data/Table_9.4_Retail_Motor_Gasoline_and_On-Highway_Diesel_Fuel_Prices.csv",
                              header=[0],
                              skiprows=[1],
                              na_values={"Not Available": np.nan,
                                         "Not Applicable": np.nan})
    oil_cols = df_oil_data.columns
    # Convert prices to float
    df_oil_data[oil_cols[1:]] = df_oil_data[oil_cols[1:]].apply(pd.to_numeric, errors='coerce')
    # Convert Month column into Year Month
    df_oil_data[['Year', 'Month']] = df_oil_data['Month'].str.split(' ', 1, expand=True)
    move_year_to_first_oil = df_oil_data.pop('Year')
    df_oil_data.insert(0, 'Year', move_year_to_first_oil)
    return df_oil_data


@st.cache
def get_avg_house_data():
    df_aspus_data = pd.read_csv("data/ASPUS.csv",
                                header=[0])
    return df_aspus_data


@st.cache
def get_median_house_data():
    df_mspus_data = pd.read_csv("data/MSPUS.csv",
                                header=[0])
    return df_mspus_data


def get_raw_house_data():
    df1 = get_avg_house_data()
    df2 = get_median_house_data()
    df2 = df2.drop(columns=['observation_date'])
    df = pd.concat([df1, df2],
                   axis=1)
    df = df.rename(columns={"ASPUS": "Average Sales Price",
                            "MSPUS": "Median Sales Price"})
    return df
