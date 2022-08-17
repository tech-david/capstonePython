import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score, auc
from model.dataset.TrainTestData import train_test_split_business_cycle
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

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


# def model_results():
#     accuracy = model_accuracy()
#     confusion_report = model_confusion_matrix_report()
#     classification_view = model_classification()
#     score = model_roc_auc_score()
#     fpr, tpr, thresholds = model_roc_curve()
#     fig, ax = plt.subplots(2, 2)
#     fig.suptitle("Model Evaluation Results")
#     ax[0, 0].add_image(confusion_report.plot())
#     ax[0, 0].set_title("Confusion Matrix")
#     ax[0, 1].plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % score)
#     ax[0, 1].set_title("Receiver Operating Characteristic Curve")
#     ax[0, 1].plot([0, 1], [0, 1], 'r--')
#     ax[0, 1].xlim([0.0, 1.0])
#     ax[0, 1].ylim([0.0, 1.05])
#     ax[0, 1].xlabel('False Positive Rate')
#     ax[0, 1].ylabel('True Positive Rate')
#     ax[1, 0].set_title("Accuracy, Precision, Recall, F1, and Support")
#     ax[1, 0].plot(accuracy)
#     ax[1, 0].plot(classification_view)
#     ax[1, 1].plot(x_train, y_train)
#     ax[1, 1].plot(x_test, y_pred)
#     ax[1, 1].scatter(x_test, y_test)
#     plots = st.pyplot(plt.show())
#     return plots
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
    equation = model.coef_
    equation = list(map('{:.3f}%'.format,equation))
    equation = np.transpose(equation)
    natural_gas_wellhead = equation[0]
    natural_gas_resident = equation[1]
    electricity_resident = equation[2]
    electricity_industrial = equation[3]
    electricity_transportation = equation[4]
    leaded_gas = equation[5]
    unleaded_gas = equation[6]
    diesel = equation[7]
    homes = equation[8]
    write = st.write(format(natural_gas_wellhead) + " NG Wellhead " +
                     format(natural_gas_resident) + " NG Residential " +
                     format(electricity_resident) + " Elec. Residential " +
                     format(electricity_industrial) + " Elec. Industrial " +
                     format(electricity_transportation) + " Ele. Transportation " +
                     format(leaded_gas) + " Leaded fuel " +
                     format(unleaded_gas) + " Unleaded fuel " +
                     format(diesel) + " Diesel " +
                     format(homes) + " Homes")
    return write
