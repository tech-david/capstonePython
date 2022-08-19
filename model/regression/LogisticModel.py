import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score, auc

from model.dataset.TrainTestData import train_test_split_business_cycle
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm


x_train, x_test, y_train, y_test = train_test_split_business_cycle()
model = LogisticRegression()
log_reg = model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_score = model.predict_proba(x_test)[:, 1]


def model_accuracy():
    accuracy = model.score(x_test, y_test)
    return accuracy


def model_confusion_matrix_report():
    report = confusion_matrix(y_test,
                              y_pred,
                              labels=model.classes_)
    return report


def model_classification():
    report = classification_report(y_test, y_pred)
    return report


def model_roc_auc_score():
    score = roc_auc_score(y_test,
                          model.predict(x_test))
    return score


def model_roc_curve():
    fpr, tpr, thresholds = roc_curve(y_test,
                                     y_score)
    return fpr, tpr, thresholds


def display_accuracy():
    accuracy = model_accuracy()
    output = st.write('Model Accuracy: {:.2f}'.format(accuracy))
    return output


def display_scores():
    report = model_confusion_matrix_report()
    df = pd.DataFrame(report,
                      columns=['Actual Positive', 'Actual Negative'],
                      index=['Predicted Positive', 'Predicted Negative'])
    plot = st.write(df)
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


# Todo make display for model
def display_predictions_plot():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=model.coef_,
                             y=y_train,
                             name="Training Data"))
    fig.update_layout(title='Real vs Predicted Values',
                      legend_title='Type of data',
                      xaxis_title='Time')
    plot = st.plotly_chart(fig,
                           use_container_width=True)
    return plot


def model_equation():
    x = model.coef_
    y = model.intercept_
    write = st.write("Rec = ",
                     str(x[:, 0]), "NG Source + ",
                     str(x[:, 1]), "NG Res + ",
                     str(x[:, 2]), "Elec Res + ",
                     str(x[:, 3]), "Elec Ind + ",
                     str(x[:, 4]), "Elec Trans + ",
                     str(x[:, 5]), "Leaded Gas+ ",
                     str(x[:, 6]), "Unleaded Gas + ",
                     str(x[:, 7]), "Diesel + ",
                     str(x[:, 8]), "Homes + ",
                     str(y)
                     )
    return write


def model_metrics():
    sm_log = sm.Logit(y_train, x_train).fit()
    write = st.write(sm_log.summary())
    return write
