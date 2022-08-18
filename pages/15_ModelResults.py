import streamlit as st

st.set_page_config(page_title="Model results",
                   layout="wide")
from model.regression.LogisticModel import display_accuracy, display_scores, display_roc_auc, model_equation

st.header("Logistic Regression Model and Results")
st.subheader("Accuracy results")
display_accuracy()
st.subheader("Confusion Matrix")
display_scores()
st.subheader("ROC-AUC Curve")
with st.container():
    display_roc_auc()

st.subheader("Logistic Regression Formula for Recession")
model_equation()
