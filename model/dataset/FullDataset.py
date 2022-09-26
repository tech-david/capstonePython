import pandas as pd
import streamlit as st
from helpers.GetRawData import get_recession_data
from model.features.PctChange import percent_change
from sklearn.preprocessing import MinMaxScaler as mms


# Putting together features and target variables
def build_features():
    df = percent_change()
    return df


def build_target():
    df = get_recession_data()
    df['DATE'] = pd.to_datetime(df['DATE']).dt.date
    df.set_index('DATE', inplace=True)
    return df


def build_dataset():
    x = build_features()
    y = build_target()
    df = x
    df = df.join(y)
    # moving target variable to beginning of dataframe
    target = df.pop('USREC')
    df.insert(0, 'USREC', target)
    return df


def render_dataset():
    df = build_dataset()
    complete_df = st.dataframe(df)
    return complete_df


# Exploration
def describe_data():
    df = build_dataset()
    df = df.describe()
    descriptive_data = st.dataframe(df)
    return descriptive_data


# Scale the data
def min_max_data():
    x = build_features()
    scale = mms()
    transformation = scale.fit_transform(x)
    df = pd.DataFrame(transformation,
                      columns=x.columns.to_list(),
                      index=x.index)
    df.interpolate(method='time',
                   limit_direction='both',
                   inplace=True)
    return df


def describe_std_data():
    df = min_max_data()
    df = df.describe()
    descriptive_data = st.dataframe(df)
    return descriptive_data
