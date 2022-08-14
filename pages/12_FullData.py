import streamlit as st

from model.dataset.FullDataset import build_dataset

st.set_page_config(page_title="Full dataset",
                   layout="wide")
st.title("Dataset With Feature Percent Changes and Target")
build_dataset()
