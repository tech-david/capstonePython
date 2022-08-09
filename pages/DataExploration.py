import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

st.set_page_config(page_title="Data Exploration",
                   layout="wide")
st.title("Economic Recessions Using Commodities")
st.markdown("Predicting recessions using common consumer commodities")
st.write(
    """Preloaded data view.  To come: Uploading own data.
    """
)

st.header("Commodities Include:")
st.markdown("> Natural gas, oil products, electricity, housing, CPI of common household goods.")
st.sidebar.header("Preloaded data exploration")


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


st.header("Natural Gas Prices Jan 1976 - Dec 2021")


def gas_raw_dataframe():
    df_gas_data = get_gas_data()
    st.subheader("Natural Gas Price Data")
    # Default columns for natural gas view
    default_cols = ['Year',
                    'Month',
                    'Natural Gas Price, Wellhead',
                    'Natural Gas Price, Citygate',
                    'Natural Gas Price, Delivered to Consumers, Residential',
                    'Natural Gas Price, Delivered to Consumers, Commercial',
                    'Percentage of Electric Power Sector Consumption for Which Price Data Are Available']
    options = df_gas_data.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_gas_data[select_options])
    return filtered_df


gas_raw_dataframe()


def gas_raw_plot():
    df = get_gas_data()
    st.subheader("Natural Gas Price Graph")
    # Creating columns for view
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
    st.subheader("Electricity Price Data")
    # Default columns for electricity view
    default_cols = ['Year',
                    'Month',
                    'Average Retail Price of Electricity, Residential',
                    'Average Retail Price of Electricity, Commercial']
    options = df_electricity_data.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_electricity_data[select_options])
    return filtered_df


def elec_raw_plot():
    df = get_electricity_data()
    st.subheader("Electricity Price Graph")
    # Creating columns for view
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
                   title='Electricity Raw Plot, Prices in ' + '\xa2' + ' per KWh (incl. tax)')
    elec_plotly_chart = st.plotly_chart(plot)
    return elec_plotly_chart


st.header("Electricity Prices Jan 1976 - Dec 2021")
elec_raw_dataframe()
elec_raw_plot()


def oil_raw_dataframe():
    df_oil_data = get_oil_data()
    st.subheader("Oil Price Data")
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Regular Motor Gasoline, All Areas, Retail Price',
                    'On-Highway Diesel Fuel Price']
    options = df_oil_data.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_oil_data[select_options])
    return filtered_df


def oil_raw_plot():
    df = get_oil_data()
    st.subheader("Oil/Fuel Price Graph")
    # Creating columns for view
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
                   title='Oil/Fuel Raw Plot, Prices in $/gal (incl. tax)')
    oil_plotly_chart = st.plotly_chart(plot)
    return oil_plotly_chart


st.header("Oil Product Prices Jan 1976 - Dec 2021")
oil_raw_dataframe()
oil_raw_plot()

# Separating out raw from cleaned data
st.header("Exploration Post Processed")
st.markdown("> Including removal of columns, and filling null values using interpolation")

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


# Dataframe for cleaned natural gas data
def post_processed_gas():
    st.subheader("Natural Gas (Cleaned) Data")
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Natural Gas Price, Delivered to Consumers, Residential',
                    'Natural Gas Price, Delivered to Consumers, Commercial'
                    ]
    options = df_gas_data_fill_na.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_gas_data_fill_na[select_options])
    return filtered_df


post_processed_gas()


def gas_clean_plot():
    df = df_gas_data_fill_na
    st.subheader("Natural Gas (Cleaned) Price Graph")
    # Creating columns for view
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
                   title='Natural Gas Cleaned Plot, Prices in $/1000 cu. ft.')
    gas_plotly_chart = st.plotly_chart(plot)
    return gas_plotly_chart


gas_clean_plot()

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


# Dataframe for cleaned electricity data
def post_processed_elec():
    st.subheader("Electricity (Cleaned) Data")
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Average Retail Price of Electricity, Residential',
                    'Average Retail Price of Electricity, Commercial'
                    ]
    options = df_electricity_data_fill_na.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_electricity_data_fill_na[select_options])
    return filtered_df


post_processed_elec()


def elec_clean_plot():
    df = df_electricity_data_fill_na
    st.subheader("Electricity (Cleaned) Price Graph")
    # Creating columns for view
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
                   title='Electricity Cleaned Plot, Prices in ' + '\xa2' + ' per KWh (incl. tax)')
    elec_plotly_chart = st.plotly_chart(plot)
    return elec_plotly_chart


elec_clean_plot()

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

# Filling out Leaded Regular Gasoline with 0 after April 1991 (no longer used) and interpolating for NA in 1976
df_oil_data_fill_na['Leaded Regular Gasoline, U.S. City Average Retail Price'] = \
    df_oil_data_fill_na.groupby(['Month'])['Leaded Regular Gasoline, U.S. City Average Retail Price'] \
        .apply(lambda x: x.interpolate(method='time', limit_direction='backward'))


# Filling out oil data with 0 rather than interpolation due to unleaded gasoline introduction
def fill_oil_with_zero(col):
    df_oil_data_fill_na[col] = df_oil_data_fill_na[col].fillna(value=0)
    return df_oil_data_fill_na


fill_oil_with_zero('Leaded Regular Gasoline, U.S. City Average Retail Price')
fill_oil_with_zero('Unleaded Regular Gasoline, U.S. City Average Retail Price')
fill_oil_with_zero('All Grades of Gasoline, U.S. City Average Retail Price')
fill_oil_with_zero('Regular Motor Gasoline, Conventional Gasoline Areas, Retail Price')
fill_oil_with_zero('Regular Motor Gasoline, Reformulated Gasoline Areas, Retail Price')
fill_oil_with_zero('Regular Motor Gasoline, All Areas, Retail Price')
fill_oil_with_zero('On-Highway Diesel Fuel Price')


def post_processed_oil():
    st.subheader("Oil (Cleaned) Data")
    # Default columns for oil view
    default_cols = ['Year',
                    'Month',
                    'Unleaded Regular Gasoline, U.S. City Average Retail Price',
                    'Regular Motor Gasoline, All Areas, Retail Price'
                    ]
    options = df_oil_data_fill_na.columns.to_list()
    select_options = st.multiselect("Select Columns to view",
                                    options,
                                    default_cols)
    filtered_df = st.dataframe(df_oil_data_fill_na[select_options])
    return filtered_df


def oil_clean_plot():
    df = df_oil_data_fill_na
    st.subheader("Oil (Cleaned) Price Graph")
    # Creating columns for view
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
                   title='Oil/Fuel Raw Plot, Prices in $/gal (incl. tax)')
    oil_plotly_chart = st.plotly_chart(plot)
    return oil_plotly_chart


post_processed_oil()
oil_clean_plot()

# Creating reports, dropping date and day, as API recreates Date
# Dropping day as it creates incorrect correlation statistics
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
natural_gas_report = st_profile_report(natural_gas_profile)
# Saving created report to folder
natural_gas_profile.to_file("reports/Natural_Gas_Reports.html")

with open("reports/Natural_Gas_Reports.html", encoding='utf8') as file:
    btn = st.download_button(
        label="Download natural gas report (HTML)",
        data=file,
        file_name="Natural_Gas_Reports.html",
        mime='text/html'
    )
