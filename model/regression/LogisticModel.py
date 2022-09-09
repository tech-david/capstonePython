import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score, auc
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import make_scorer
from sklearn.feature_selection import SelectFromModel

from model.dataset.TrainTestData import train_test_split_business_cycle
import streamlit as st
import plotly.express as px
import statsmodels.api as sm

from helpers.Metrics import rmse, regression_results

# Get Split Data
x_train, x_test, y_train, y_test = train_test_split_business_cycle()
# Create Cross Validation
tscv = TimeSeriesSplit(n_splits=9)
# Initiate Model
model = LogisticRegression()
# Create scorer
rmse_score = make_scorer(rmse, greater_is_better=True)
# Create parameter map for grid model comparison
param_map = {
    "solver": ['liblinear', 'lbfgs'],
    "max_iter": [100, 200],
    "warm_start": [False, True]
}
# Grid search to test all models based on hyperparameters
gsearch = GridSearchCV(estimator=model,
                       cv=tscv,
                       param_grid=param_map,
                       scoring=rmse_score)
gsearch.fit(x_train, y_train)


def best_score_after_tscv():
    best_score = gsearch.best_score_
    return best_score


def what_best_model():
    best_model = gsearch.best_estimator_
    return best_model


def results_after_tscv():
    best_model = gsearch.best_estimator_
    y_true = y_test.values
    y_best = best_model.predict(x_test)
    results = regression_results(y_true, y_best)
    return results


def model_accuracy():
    best_model = what_best_model()
    accuracy = best_model.score(x_test, y_test)
    return accuracy


def model_confusion_matrix_report():
    best_model = gsearch.best_estimator_
    y_true = y_test.values
    y_best = best_model.predict(x_test)
    report = confusion_matrix(y_true,
                              y_best,
                              labels=best_model.classes_)
    return report


def model_classification():
    best_model = what_best_model()
    y_pred = best_model.predict(x_test)
    report = classification_report(y_test, y_pred)
    table = st.text('Model Report:\n ' + report)
    return table


def model_roc_auc_score():
    best_model = gsearch.best_estimator_
    score = roc_auc_score(y_test,
                          best_model.predict(x_test))
    return score


def model_roc_curve():
    y_best_model = gsearch.best_estimator_.predict_proba(x_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test,
                                     y_best_model)
    return fpr, tpr, thresholds


def display_accuracy():
    accuracy = model_accuracy()
    output = st.write('Model Accuracy: {:.2f}'.format(accuracy))
    return output


def display_scores():
    report = model_confusion_matrix_report()
    matrix_df = pd.DataFrame(report,
                             columns=['Actual Positive', 'Actual Negative'],
                             index=['Predicted Positive', 'Predicted Negative'])
    plot = st.write(matrix_df)
    return plot


def display_roc_auc():
    fpr, tpr, threshold = model_roc_curve()
    fig = px.area(x=fpr,
                  y=tpr,
                  title=f'ROC Curve (AUC={auc(fpr, tpr):.4f})',
                  labels=dict(x='False Positive Rate',
                              y='True Positive Rate'),
                  width=700,
                  height=600)
    fig.add_shape(type='line',
                  line=dict(dash='dash'),
                  x0=0,
                  x1=1,
                  y0=0,
                  y1=1)
    fig.update_xaxes(scaleanchor="x",
                     scaleratio=1)
    fig.update_yaxes(constrain='domain')
    plot = st.plotly_chart(fig,
                           use_container_width=True)
    return plot


def model_metrics():
    sm_log = sm.Logit(y_train, x_train).fit()
    write = st.write(sm_log.summary())
    return write


def return_pred():
    best_model = what_best_model()
    predictions = best_model.predict(x_test)
    return predictions


def return_test():
    test = y_test
    return test


def best_features():
    features = SelectFromModel(gsearch.best_estimator_)
    features.fit(x_train, y_train)
    feature_idx = features.get_support()
    df_feature_idx = pd.DataFrame(feature_idx,
                                  columns=['Best?'],
                                  dtype=bool)
    df_features = pd.DataFrame(gsearch.feature_names_in_,
                               columns=['Feature'])
    df_best_features = pd.concat([df_features, df_feature_idx], axis=1)
    feature_name = st.write(df_best_features)
    return feature_name
