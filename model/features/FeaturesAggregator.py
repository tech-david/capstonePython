import streamlit as st

from helpers.Cleaner import fill_gas_na, fill_electricity_na, fill_oil_na, resample_house


def get_all_features():
    # Getting common columns to drop
    col = ['Year', 'Month', 'Day', 'Date']
    df_ng = fill_gas_na()
    df_ng.drop(columns=col, inplace=True)
    df_elec = fill_electricity_na()
    df_elec.drop(columns=col, inplace=True)
    df_oil = fill_oil_na()
    df_oil.drop(columns=col, inplace=True)
    df_house = resample_house()

    df = df_ng
    df = df.merge(df_elec, how='outer', on='Date', sort=True)
    df = df.merge(df_oil, how='outer', on='Date', sort=True)
    df = df.join(df_house)
    return df
