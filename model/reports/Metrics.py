from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import streamlit as st
from model.dataset.FullDataset import min_max_data, build_target
from model.features.Preparation import drop_high_vif


# compute the vif for all given features
def calculate_vif():
    # the independent variables set
    x = min_max_data()
    # target dummy
    y = build_target()
    x.fillna(value=0,
             inplace=True)
    df = x
    df = df.join(y)
    target = df.pop('USREC')
    df.insert(0, 'USREC', target)
    df.fillna(value=0,
              inplace=True)
    df['USREC'] = df['USREC'].map({1: 'Recession', 0: 'No Recession'})

    # VIF dataframe
    vif_data = pd.DataFrame()
    vif_data["feature"] = x.columns

    # calculating VIF for each feature
    vif_data["VIF"] = [variance_inflation_factor(x.values, i)
                       for i in range(len(x.columns))]
    plot = st.write(vif_data)
    return plot


def calculate_vif_after():
    # the independent variables set
    x = drop_high_vif()
    # target dummy
    y = build_target()
    x.fillna(value=0,
             inplace=True)
    df = x
    df = df.join(y)
    target = df.pop('USREC')
    df.insert(0, 'USREC', target)
    df.fillna(value=0,
              inplace=True)
    df['USREC'] = df['USREC'].map({1: 'Recession', 0: 'No Recession'})

    # VIF dataframe
    vif_data = pd.DataFrame()
    vif_data["feature"] = x.columns

    # calculating VIF for each feature
    vif_data["VIF"] = [variance_inflation_factor(x.values, i)
                       for i in range(len(x.columns))]
    plot = st.write(vif_data)
    return plot
