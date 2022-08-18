import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("# Economic Recession Using Consumer Commodities")

st.sidebar.header("Home")
st.markdown(
    """
    Using consumer facing commodities prices to predict recessions using logistical regression.  Visit the **_About_**
    page on the sidebar to read more info.
    ## Pages
    ### Home
    - You are here. 
    ### About
    - Navigate to 'About'
      - Provides information about application and its use.
    ### DataExploration
    - Raw data exploration, consists of interactive dataframes and plots
    ### Processed Data Exploration
    - Data that has gone through initial phase of cleaning, which includes interpolation and filling NA with 0 where appropriate.
    ### Reports
    - Reports generated from datasets that include statistical metrics such as quartiles, mean, median, standard deviation
    and more.
    - Natural Gas
    - Electricity
    - Oil
    - Home
    - Feature
    - Model Data
    ### Feature Exploration
    - Features that have been extracted through monthly price changes of each variable.
    ### Standardized Data
    - Price changes after standardization.
    ### Model Data
    - Data ready for the model, exploration includes correlation maps and variance inflation factor metric.
    ### Train Test Split
    - Data after being split into training and testing data sets.  Testing data was split from the most recent 5 year window, representative of a typical business cyccle.
    ### Model Results
    - Statistical results of the model tested, current reports include accuracy, confusion matrix, and ROC curve.  More reports to come including R2, and p-value metrics.
    """)
