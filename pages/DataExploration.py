from datetime import datetime
from sys import path

import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

st.set_page_config(page_title="Data Exploration")
st.title("Economic Recessions Using Commodities")
st.markdown("Predicting recessions using common consumer commodities")
st.write(
    """Preloaded data view.  To come: Uploading own data.
    """
)

st.header("Commodities Include:")
st.markdown("> Natural gas, oil products, electricity, housing, CPI of common household goods.")
st.sidebar.header("Preloaded data exploration")


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
    df_electricity_data[elec_cols[1:]] = df_electricity_data[elec_cols[1:]].apply(pd.to_numeric, errors='coerce')
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
    df_oil_data[oil_cols[1:]] = df_oil_data[oil_cols[1:]].apply(pd.to_numeric, errors='coerce')
    df_oil_data[['Year', 'Month']] = df_oil_data['Month'].str.split(' ', 1, expand=True)
    move_year_to_first_oil = df_oil_data.pop('Year')
    df_oil_data.insert(0, 'Year', move_year_to_first_oil)
    return df_oil_data


st.header("Natural Gas Prices Jan 1976 - Dec 2021")


def gas_raw_dataframe():
    df_gas_data = get_gas_data()
    st.subheader("Natural gas price data")
    # Default columns for natural gas view
    natural_gas_columns = ['Year',
                           'Month',
                           'Natural Gas Price, Wellhead',
                           'Natural Gas Price, Citygate',
                           'Natural Gas Price, Delivered to Consumers, Residential',
                           'Natural Gas Price, Delivered to Consumers, Commercial',
                           'Percentage of Electric Power Sector Consumption for Which Price Data Are Available']
    options = df_gas_data.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    natural_gas_columns)
    filtered_df = st.dataframe(df_gas_data[select_options])
    return filtered_df


gas_raw_dataframe()


def gas_raw_plot():
    df = get_gas_data()
    st.subheader("Natural gas price graph")
    col1, col2 = st.columns(2)
    x_axis = col1.selectbox('Select X-axis',
                            options=df.columns)
    y_axis = col2.selectbox('Select Y-axis',
                            options=df.columns)
    plot = px.area(df,
                   x=x_axis,
                   y=y_axis,
                   line_group='Month',
                   color='Month',
                   title='Natural Gas Raw Plot, Prices in $/1000 cu. ft.')
    gas_plotly_chart = st.plotly_chart(plot)
    return gas_plotly_chart


gas_raw_plot()


def elec_raw_dataframe():
    df_electricity_data = get_electricity_data()
    st.subheader("Electricity price data")
    # Default columns for electricity view
    electricity_columns = ['Year',
                           'Month',
                           'Average Retail Price of Electricity, Residential',
                           'Average Retail Price of Electricity, Commercial']
    options = df_electricity_data.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    electricity_columns)
    filtered_df = st.dataframe(df_electricity_data[select_options])
    return filtered_df


def elec_raw_plot():
    df = get_electricity_data()
    st.subheader("Electricity price graph")
    col1, col2 = st.columns(2)
    x_axis = col1.selectbox('Select X-axis',
                            options=df.columns)
    y_axis = col2.selectbox('Select Y-axis',
                            options=df.columns)
    plot = px.area(df,
                   x=x_axis,
                   y=y_axis,
                   line_group='Month',
                   color='Month',
                   title='Natural Gas Raw Plot, Prices in' + '\xa2' + 'per KWh (incl. tax)')
    elec_plotly_chart = st.plotly_chart(plot)
    return elec_plotly_chart


st.header("Electricity Prices Jan 1976 - Dec 2021")
elec_raw_dataframe()
elec_raw_plot()

st.header("Oil Product Prices Jan 1976 - Dec 2021")
st.dataframe(df_oil_data)

oil_default_cols = ['Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Regular Motor Gasoline, All Areas, Retail Price',
                    'On-Highway Diesel Fuel Price']
st_ms_oil = st.multiselect("Columns",
                           df_oil_data.columns.to_list(),
                           oil_default_cols)
st.header("Fuel price graphs")
fig_oil = px.area(df_oil_data,
                  x='Year',
                  y='Unleaded Regular Gasoline, U.S. City Average Retail Price',
                  line_group='Month',
                  color='Month',
                  title='Unleaded Regular Gasoline, U.S. City Average Retail Price',
                  labels={'Unleaded Regular Gasoline, U.S. City Average Retail Price': '$/gal (incl. tax)'})
st.plotly_chart(fig_oil)

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


# Helper method to fill NA values using interpolation
def fill_gas_na(col):
    df_gas_data_fill_na[col] = df_gas_data_fill_na.groupby(['Month'])[col] \
        .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    return df_gas_data_fill_na


# Fill columns
fill_gas_na('Natural Gas Price, Delivered to Consumers, Residential')
fill_gas_na('Natural Gas Price, Wellhead')
fill_gas_na('Natural Gas Price, Citygate')
fill_gas_na('Natural Gas Price, Delivered to Consumers, Commercial')
fill_gas_na('Natural Gas Price, Delivered to Consumers, Industrial')
fill_gas_na('Natural Gas Price, Electric Power Sector')

st.dataframe(df_gas_data_fill_na)
fig_natural_gas = px.area(df_gas_data_fill_na,
                          x='Year',
                          y='Natural Gas Price, Delivered to Consumers, Residential',
                          line_group='Month',
                          color='Month',
                          title='Natural Gas Price, Delivered to Consumers, Residential',
                          labels={'Natural Gas Price, Delivered to Consumers, Residential': '$/1000 cu. ft.'})
st.plotly_chart(fig_natural_gas)

# Copy electricity data to start cleaning
df_electricity_data_fill_na = df_electricity_data
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
df_electricity_data_fill_na = df_electricity_data_fill_na.drop(columns=['Average Retail Price of Electricity, Other'])


# Helper method to fill using interpolation
def fill_electricity_na(col):
    df_electricity_data_fill_na[col] = df_electricity_data_fill_na.groupby(['Month'])[col] \
        .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
    return df_electricity_data_fill_na


fill_electricity_na('Average Retail Price of Electricity, Residential')
fill_electricity_na('Average Retail Price of Electricity, Commercial')
fill_electricity_na('Average Retail Price of Electricity, Industrial')
fill_electricity_na('Average Retail Price of Electricity, Transportation')
fill_electricity_na('Average Retail Price of Electricity, Total')
st.dataframe(df_electricity_data_fill_na)

# Copy oil data to start cleaning
df_oil_data_fill_na = df_oil_data
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
print(df_oil_data_fill_na.dtypes)

# Helper method to fill using zeros (Not Applicable data)
# ToDo find a way to replace data values with 0
# def fill_oil_not_applicable(col, year):
#     if df_oil_data_fill_na.loc[df_oil_data_fill_na['Year'] > year and df_oil_data_fill_na[col].isnull():
#         df_oil_data_fill_na = df_oil_data_fill_na[col].insert(0)
#         return df_oil_data_fill_na
#     return df_oil_data_fill_na


# Helper method to fill using interpolation
# def fill_oil_not_available(col):
#     df_oil_data_fill_na[col] = df_oil_data_fill_na.groupby(['Month'])[col] \
#         .apply(lambda x: x.interpolate(method='time', limit_direction='both'))
#     return df_oil_data_fill_na
#
#
# st.dataframe(df_oil_data_fill_na)
# fill_oil_not_applicable('Unleaded Regular Gasoline, U.S. City Average Retail Price', 1975)

natural_gas_profile = ProfileReport(df_gas_data_fill_na.drop(columns=['Date', 'Day']),
                                    title="Natural Gas Reports",
                                    dataset={
                                        "description": "Reports of cleaned natural gas dataset"
                                    },
                                    variables={
                                        "descriptions": {
                                            "Natural Gas Price, Wellhead": "Price from source",
                                            "Natural Gas Price, Citygate": "Point of distribution",
                                            "Natural Gas Price, Delivered to Consumers, Residential": "Average price "
                                                                                                      "paid for by "
                                                                                                      "residential "
                                                                                                      "users ",
                                            "Natural Gas Price, Delivered to Consumers, Commercial": "Average price "
                                                                                                     "paid for by "
                                                                                                     "commercial "
                                                                                                     "users ",
                                            "Natural Gas Price, Delivered to Consumers, Industrial": "Average price "
                                                                                                     "paid for by "
                                                                                                     "industrial "
                                                                                                     "users ",
                                        }
                                    })

st.title("Reports of natural gas data after filling NA values")
st_profile_report(natural_gas_profile)
natural_gas_profile.to_file(path("reports/Natural_Gas_Reports.html"))
