from helpers.Cleaner import fill_electricity_na, fill_gas_na, fill_oil_na
from helpers.GetRawData import get_gas_data, get_electricity_data, get_oil_data
import streamlit as st
import plotly.express as px


def gas_raw_plot():
    df = get_gas_data()
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


def elec_raw_plot():
    df = get_electricity_data()
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


def oil_raw_plot():
    df = get_oil_data()
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


def gas_clean_plot():
    df = fill_gas_na()
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


def elec_clean_plot():
    df = fill_electricity_na()
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


def oil_clean_plot():
    df = fill_oil_na()
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
