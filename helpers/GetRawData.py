import streamlit as st
import pandas as pd
import numpy as np
import glob

# Helper file to get raw data

from helpers.S3Connector import connect

# Establish connection to S3 bucket
s3 = connect()
BUCKET = 'capstoneds2022data'


# Using cache to save resources
@st.cache
def get_gas_data():
    obj = s3.Bucket(BUCKET).Object('data/Table_9.10_Natural_Gas_Prices.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0],
                     skiprows=[1],
                     na_values="Not Available")

    cols = df.columns
    # Convert prices to float
    df[cols[1:]] = df[cols[1:]].apply(pd.to_numeric,
                                      errors='coerce')
    # Convert Month column into Year Month
    df[['Year', 'Month']] = df['Month'].str.split(' ',
                                                  1,
                                                  expand=True)
    move_year_to_first = df.pop('Year')
    df.insert(0,
              'Year',
              move_year_to_first)
    return df


@st.cache
def get_electricity_data():
    obj = s3.Bucket(BUCKET).Object('data/Table_9.8_Average_Retail_Prices_of_Electricity.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0],
                     skiprows=[1],
                     na_values="Not Available")
    cols = df.columns
    # Convert prices to float
    df[cols[1:]] = df[cols[1:]].apply(pd.to_numeric, errors='coerce')
    # Convert Month column into Year Month
    df[['Year', 'Month']] = df['Month'].str.split(' ', 1, expand=True)
    move_year_to_first_elec = df.pop('Year')
    df.insert(0, 'Year', move_year_to_first_elec)
    return df


@st.cache
def get_oil_data():
    obj = s3.Bucket(BUCKET).Object('data/Table_9.4_Retail_Motor_Gasoline_and_On-Highway_Diesel_Fuel_Prices.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0],
                     skiprows=[1],
                     na_values={"Not Available": np.nan,
                                "Not Applicatble": np.nan})
    cols = df.columns
    # Convert prices to float
    df[cols[1:]] = df[cols[1:]].apply(pd.to_numeric, errors='coerce')
    # Convert Month column into Year Month
    df[['Year', 'Month']] = df['Month'].str.split(' ', 1, expand=True)
    move_year_to_first_oil = df.pop('Year')
    df.insert(0, 'Year', move_year_to_first_oil)
    return df


@st.cache
def get_avg_house_data():
    obj = s3.Bucket(BUCKET).Object('data/ASPUS.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0])
    return df


@st.cache
def get_median_house_data():
    obj = s3.Bucket(BUCKET).Object('data/MSPUS.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0])
    return df


def get_raw_house_data():
    df1 = get_avg_house_data()
    df2 = get_median_house_data()
    df2 = df2.drop(columns=['DATE'])
    df = pd.concat([df1, df2],
                   axis=1)
    df = df.rename(columns={"ASPUS": "Average Sales Price",
                            "MSPUS": "Median Sales Price"})
    return df


def get_recession_data():
    obj = s3.Bucket(BUCKET).Object('data/USREC.csv').get()
    df = pd.read_csv(obj['Body'],
                     header=[0])
    return df


@st.cache
def get_cpi_data():
    # navigate to folder
    path = 'data/cpi'
    # get list of files
    files = glob.glob(path + "/*.csv")
    # create datasets for files
    df = pd.DataFrame(columns=['Year', 'Period'])
    # Create dictionary to reformat months
    month_dict = {"M01": "1",
                  "M02": "2",
                  "M03": "3",
                  "M04": "4",
                  "M05": "5",
                  "M06": "6",
                  "M07": "7",
                  "M08": "8",
                  "M09": "9",
                  "M10": "10",
                  "M11": "11",
                  "M12": "12"}

    bucket = s3.Bucket(BUCKET)
    for obj in bucket.objects.filter(Prefix='data/cpi'):
        file = s3.Bucket(BUCKET).Object(obj.key).get()
        obj_df = pd.read_csv(file['Body'],
                             usecols=['Year', 'Period', 'Value'],
                             index_col=None,
                             header=0)
        # Creating column names based on CPI item
        # Get object key and remove prefix
        col_name = obj.key.removeprefix(r"data/cpi/")
        # Remove file extension
        col_name = col_name.removesuffix(r".csv")
        col_name = col_name.replace("\\", "")
        # Rename value column to CPI item
        obj_df.rename(columns={'Value': col_name},
                      inplace=True)
        # Merge with global dataframe
        df = df.merge(obj_df,
                      how='outer')

    # sort in chronological order
    df.sort_values(by=['Year', 'Period'],
                   inplace=True,
                   ignore_index=True)
    df.reset_index()
    # replace month values with dictionary
    df.replace({'Period': month_dict},
               inplace=True)
    return df
