import pandas as pd
import numpy as np
from helpers.GetRawData import get_gas_data, get_electricity_data, get_oil_data, get_raw_house_data

# Data cleaning
# Dictionary for Month
month_dict = {"January": 1,
              "February": 2,
              "March": 3,
              "April": 4,
              "May": 5,
              "June": 6,
              "July": 7,
              "August": 8,
              "September": 9,
              "October": 10,
              "November": 11,
              "December": 12}


def resample_gas():
    # Copy gas data to start cleaning
    df_gas_data_fill_na = get_gas_data()
    # Replacing month strings with dictionary
    df_gas_data_fill_na = df_gas_data_fill_na.replace({'Month': month_dict})
    # Creating datetime index for resample
    df_gas_data_fill_na['Day'] = np.ones((552, 1))
    df_gas_data_fill_na['Day'] = df_gas_data_fill_na['Day'].fillna('1')
    df_gas_data_fill_na['Date'] = pd.to_datetime(df_gas_data_fill_na[['Year', 'Month', 'Day']])
    df_gas_data_fill_na.index = df_gas_data_fill_na['Date']
    df_gas_data_fill_na = pd.DataFrame(df_gas_data_fill_na,
                                       index=df_gas_data_fill_na['Date'])
    # Dropping columns not related to price (Transportation all NA)
    df_gas_data_fill_na = df_gas_data_fill_na.drop(
        columns=['Percentage of Residential Sector Consumption for Which Price Data Are Available',
                 'Percentage of Commercial Sector Consumption for Which Price Data Are Available',
                 'Percentage of Electric Power Sector Consumption for Which Price Data Are Available',
                 'Percentage of Industrial Sector Consumption for Which Price Data Are Available',
                 'Natural Gas Transportation Sector Price'])
    return df_gas_data_fill_na


# Helper method to fill NA values using interpolation
def fill_gas_na():
    df = resample_gas()
    df['Natural Gas Price, Delivered to Consumers, Residential'] = \
        df.groupby(['Month'])['Natural Gas Price, Delivered to Consumers, Residential'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    df['Natural Gas Price, Wellhead'] = \
        df.groupby(['Month'])['Natural Gas Price, Wellhead'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    df['Natural Gas Price, Citygate'] = \
        df.groupby(['Month'])['Natural Gas Price, Citygate'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    df['Natural Gas Price, Delivered to Consumers, Commercial'] = \
        df.groupby(['Month'])['Natural Gas Price, Delivered to Consumers, Commercial'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    df['Natural Gas Price, Delivered to Consumers, Industrial'] = \
        df.groupby(['Month'])['Natural Gas Price, Delivered to Consumers, Industrial'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    df['Natural Gas Price, Electric Power Sector'] = \
        df.groupby(['Month'])['Natural Gas Price, Electric Power Sector'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    return df


def resample_elec():
    # Copy electricity data to start cleaning
    df_electricity_data_fill_na = get_electricity_data()
    # Replacing month strings with dictionary
    df_electricity_data_fill_na = df_electricity_data_fill_na.replace({'Month': month_dict})
    # Creating datetime index for resample
    df_electricity_data_fill_na['Day'] = np.ones((552, 1))
    df_electricity_data_fill_na['Day'] = df_electricity_data_fill_na['Day'].fillna('1')
    df_electricity_data_fill_na['Date'] = pd.to_datetime(df_electricity_data_fill_na[['Year', 'Month', 'Day']])
    df_electricity_data_fill_na.index = df_electricity_data_fill_na['Date']
    df_electricity_data_fill_na = pd.DataFrame(df_electricity_data_fill_na,
                                               index=df_electricity_data_fill_na['Date'])
    # Dropping 'Other' Category
    df_electricity_data_fill_na = df_electricity_data_fill_na.drop(
        columns=['Average Retail Price of Electricity, Other'])
    return df_electricity_data_fill_na


# Helper method to fill using interpolation
def fill_electricity_na():
    df = resample_elec()
    df['Average Retail Price of Electricity, Industrial'] = \
        df.groupby(['Month'])['Average Retail Price of Electricity, Industrial'] \
            .apply(lambda x: x.interpolate(method='linear', limit_direction='backward'))
    df['Average Retail Price of Electricity, Residential'] = \
        df.groupby(['Month'])['Average Retail Price of Electricity, Residential'] \
            .apply(lambda x: x.interpolate(method='linear', limit_direction='backward'))
    df['Average Retail Price of Electricity, Commercial'] = \
        df.groupby(['Month'])['Average Retail Price of Electricity, Commercial'] \
            .apply(lambda x: x.interpolate(method='linear', limit_direction='backward'))
    df['Average Retail Price of Electricity, Total'] = \
        df.groupby(['Month'])['Average Retail Price of Electricity, Total'] \
            .apply(lambda x: x.interpolate(method='linear', limit_direction='backward'))
    return df


def resample_oil():
    # Copy oil data to start cleaning
    df_oil_data_fill_na = get_oil_data()
    # Replacing month strings with dictionary
    df_oil_data_fill_na = df_oil_data_fill_na.replace({'Month': month_dict})
    # Creating datetime index for resample
    df_oil_data_fill_na['Day'] = np.ones((590, 1))
    df_oil_data_fill_na['Day'] = df_oil_data_fill_na['Day'].fillna('1')
    df_oil_data_fill_na['Date'] = pd.to_datetime(df_oil_data_fill_na[['Year', 'Month', 'Day']])
    df_oil_data_fill_na.index = df_oil_data_fill_na['Date']
    df_oil_data_fill_na = pd.DataFrame(df_oil_data_fill_na,
                                       index=df_oil_data_fill_na['Date'])
    # Converting years from strings to integers for help method
    df_oil_data_fill_na['Year'] = df_oil_data_fill_na['Year'].astype(int)
    return df_oil_data_fill_na


def fill_oil_na():
    df = resample_oil()
    # Filling out Leaded Regular Gasoline with 0 after April 1991 (no longer used) and interpolating for NA in 1976
    df['Leaded Regular Gasoline, U.S. City Average Retail Price'] = \
        df.groupby(['Month'])['Leaded Regular Gasoline, U.S. City Average Retail Price'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='backward'))
    df['All Grades of Gasoline, U.S. City Average Retail Price'] = \
        df.groupby(['Month'])['All Grades of Gasoline, U.S. City Average Retail Price'] \
            .apply(lambda x: x.interpolate(method='time', limit_direction='backward'))
    return df


def resample_house():
    df = get_raw_house_data()
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    df.set_index('observation_date', inplace=True)
    # Resampling from quarterly to monthly start data, then filling NA with interpolation
    df = df.resample('MS').interpolate(method='linear', limit_direction='backward')
    return df
