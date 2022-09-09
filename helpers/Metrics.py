import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import streamlit as st
import sklearn.metrics as metrics
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


def rmse(actual, predict):
    predict = np.array(predict)
    actual = np.array(actual)
    distance = predict - actual
    squared_distance = distance ** 2
    mean_square_distance = squared_distance.mean()
    score = np.sqrt(mean_square_distance)
    return score


def regression_results(y_true, y_pred):
    variance = metrics.explained_variance_score(y_true, y_pred)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    msle = metrics.mean_squared_log_error(y_true, y_pred)
    mse = metrics.mean_squared_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    # p_values = metrics.
    print('Explained vairance: ', round(variance, 4))
    print('Mean Squared Log Error: ', round(msle, 4))
    print('R2: ', round(r2, 4))
    print('MAE: ', round(mae, 4))
    print('MSE: ', round(mse, 4))
    print('RMSE: ', round(np.sqrt(mse), 4))
