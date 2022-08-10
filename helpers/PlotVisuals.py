from helpers.Cleaner import fill_electricity_na, fill_gas_na, fill_oil_na, resample_house
from helpers.GetRawData import get_gas_data, get_electricity_data, get_oil_data, get_raw_house_data, get_recession_data
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


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


def house_raw_plot():
    df = get_raw_house_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['observation_date'],
                             y=df["Average Sales Price"],
                             fill='tonexty',
                             name='Average Sales Price'))
    fig.add_trace(go.Scatter(x=df['observation_date'],
                             y=df["Median Sales Price"],
                             fill='tozeroy',
                             name='Median Sales Price'))
    fig.update_layout(
        title='Price of Homes in $',
        legend_title='Type of price',
        xaxis_title='Time',
        yaxis_title='Dollars ($)'
    )
    house_plotly_chart = st.plotly_chart(fig)
    return house_plotly_chart


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


def house_clean_plot():
    df = resample_house()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,
                             y=df["Average Sales Price"],
                             fill='tonexty',
                             name='Average Sales Price'))
    fig.add_trace(go.Scatter(x=df.index,
                             y=df["Median Sales Price"],
                             fill='tozeroy',
                             name='Median Sales Price'))
    fig.update_layout(
        title='Price of Homes in $',
        legend_title='Type of price',
        xaxis_title='Time',
        yaxis_title='Dollars ($)'
    )
    house_plotly_chart = st.plotly_chart(fig)
    return house_plotly_chart


def recession_raw_plot():
    df = get_recession_data()
    fig = go.Figure()
    fig.add_scatter(x=df['DATE'],
                    y=df['USREC'])
    fig.update_layout(
        title='NBER Indicated Recession',
        xaxis_title='Time',
        yaxis_title='Recession (1: Recession, 0: No Recession)'
    )
    recession_plotly_chart = st.plotly_chart(fig)
    return recession_plotly_chart
