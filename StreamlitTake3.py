from datetime import datetime

import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


@st.cache
def get_gas_data():
    return pd.read_csv(r"C:\Users\David's PC\OneDrive - Grand Canyon "
                       r"University\Capstone\Backend\capstonePython\capstonePython\data\Table_9.10_Natural_Gas_Prices"
                       r".csv",
                       header=[0],
                       skiprows=[1],
                       na_values="Not Available")


@st.cache
def get_electricity_data():
    return pd.read_csv(r"C:\Users\David's PC\OneDrive - Grand Canyon "
                       r"University\Capstone\Backend\capstonePython\capstonePython\data\Table_9"
                       r".8_Average_Retail_Prices_of_Electricity.csv",
                       header=[0],
                       skiprows=[1],
                       na_values="Not Available")


@st.cache
def get_oil_data():
    return pd.read_csv(r"C:\Users\David's PC\OneDrive - Grand Canyon "
                       r"University\Capstone\Backend\capstonePython\capstonePython\data\Table_9"
                       r".4_Retail_Motor_Gasoline_and_On-Highway_Diesel_Fuel_Prices.csv",
                       header=[0],
                       skiprows=[1],
                       na_values="Not Available")


df_gas_data = get_gas_data()
df_electricity_data = get_electricity_data()
df_oil_data = get_oil_data()
# Convert prices to float
ng_cols = df_gas_data.columns
df_gas_data[ng_cols[1:]] = df_gas_data[ng_cols[1:]].apply(pd.to_numeric, errors='coerce')
elec_cols = df_electricity_data.columns
df_electricity_data[elec_cols[1:]] = df_electricity_data[elec_cols[1:]].apply(pd.to_numeric, errors='coerce')
oil_cols = df_oil_data.columns
df_oil_data[oil_cols[1:]] = df_oil_data[oil_cols[1:]].apply(pd.to_numeric, errors='coerce')

# Convert Month columnn into Year Month
df_gas_data[['Year', 'Month']] = df_gas_data['Month'].str.split(' ', 1, expand=True)
move_year_to_first = df_gas_data.pop('Year')
df_gas_data.insert(0, 'Year', move_year_to_first)
df_electricity_data[['Year', 'Month']] = df_electricity_data['Month'].str.split(' ', 1, expand=True)
move_year_to_first_elec = df_electricity_data.pop('Year')
df_electricity_data.insert(0, 'Year', move_year_to_first_elec)
df_oil_data[['Year', 'Month']] = df_oil_data['Month'].str.split(' ', 1, expand=True)
move_year_to_first_oil = df_oil_data.pop('Year')
df_oil_data.insert(0, 'Year', move_year_to_first_oil)

st.title("Economic Recessions Using Commodities")
st.markdown("Predicting recessions using common consumer commodities")

st.header("Commodities Include:")
st.markdown("> Natural gas, oil products, electricity, housing, CPI of common household goods.")

st.header("Natural Gas Prices Jan 1976 - Dec 2021")
st.dataframe(df_gas_data)

# Default columns for natural gas view
natural_gas_columns = ['Natural Gas Price, Wellhead',
                       'Natural Gas Price, Citygate',
                       'Natural Gas Price, Delivered to Consumers, Residential',
                       'Natural Gas Price, Delivered to Consumers, Commercial',
                       'Percentage of Electric Power Sector Consumption for Which Price Data Are Available']
st_ms_natural_gas = st.multiselect("Columns",
                                   df_gas_data.columns.to_list(),
                                   natural_gas_columns)
st.header("Natural gas price graphs")
fig_natural_gas = px.area(df_gas_data,
                          x='Year',
                          y='Natural Gas Price, Delivered to Consumers, Residential',
                          line_group='Month',
                          color='Month',
                          title='Natural Gas Price, Delivered to Consumers, Residential',
                          labels={'Natural Gas Price, Delivered to Consumers, Residential': '$/1000 cu. ft.'})
st.plotly_chart(fig_natural_gas)

st.header("Electricity Prices Jan 1976 - Dec 2021")
st.dataframe(df_electricity_data)

# Default columns for electricity view
electricity_columns = ['Average Retail Price of Electricity, Residential',
                       'Average Retail Price of Electricity, Commercial']
st_ms_electricity = st.multiselect("Columns",
                                   df_electricity_data.columns.to_list(),
                                   electricity_columns)
st.header("Electricity price graphs")
fig_electricity = px.area(df_electricity_data,
                          x='Year',
                          y='Average Retail Price of Electricity, Residential',
                          line_group='Month',
                          color='Month',
                          title='Average Retail Price of Electricity, Residential',
                          labels={'Average Retail Price of Electricity, Residential': '\xa2' + ' per KWh (incl. tax)'})
st.plotly_chart(fig_electricity)

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
# Interpolation to fill NA values
df_gas_data_fill_na = df_gas_data
# Replacing month strings with dictionary
df_gas_data_fill_na = df_gas_data_fill_na.replace({'Month': month_dict})
# Creating datetime index for resample
df_gas_data_fill_na['Day'] = np.ones((552, 1))
df_gas_data_fill_na['Day'] = df_gas_data_fill_na['Day'].fillna('1')
df_gas_data_fill_na['Date'] = pd.to_datetime(df_gas_data_fill_na[['Year', 'Month', 'Day']])
df_gas_data_fill_na.index = df_gas_data_fill_na['Date']
# df_gas_data_fill_na.drop(['Year',
#                           'Month',
#                           'Percentage of Residential Sector Consumption for Which Price Data Are Available',
#                           'Percentage of Commercial Sector Consumption for Which Price Data Are Available',
#                           'Percentage of Industrial Sector Consumption for Which Price Data Are Available',
#                           'Percentage of Electric Power Sector Consumption for Which Price Data Are Available',
#                           'Day'],
#                          axis=1,
#                          inplace=True)
df_gas_data_fill_na = pd.DataFrame(df_gas_data_fill_na,
                                   index=df_gas_data_fill_na['Date'])
# df_gas_data_fill_na['Natural Gas Price, Citygate'].interpolate(method='time',
#                                                                limit_direction='backward',
#                                                                inplace=True,
#                                                                downcast='infer')

df_gas_data_fill_na['Natural Gas Price, Delivered to Consumers, Residential'] = \
    df_gas_data_fill_na.groupby('Month')['Natural Gas Price, Delivered to Consumers, Residential'] \
        .apply(lambda x: x.interpolate(method='time',
                                       limit_direction='backward'))
st.dataframe(df_gas_data_fill_na)
fig_natural_gas = px.area(df_gas_data_fill_na,
                          x='Year',
                          y='Natural Gas Price, Delivered to Consumers, Residential',
                          line_group='Month',
                          color='Month',
                          title='Natural Gas Price, Delivered to Consumers, Residential',
                          labels={'Natural Gas Price, Delivered to Consumers, Residential': '$/1000 cu. ft.'})
st.plotly_chart(fig_natural_gas)