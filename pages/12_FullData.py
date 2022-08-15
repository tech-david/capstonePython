import streamlit as st
from model.features.Correltaion import complete_df

st.set_page_config(page_title="Full dataset",
                   layout="wide")
st.title("Dataset that will be used in model")
st.markdown(">Data mutation events")
st.markdown("""
            - Percent change
            - Standardized
            - Dropped High Correlation
            - Filled NAN with interpolation
            """)
st.subheader("Dataset")
st.write(complete_df())
