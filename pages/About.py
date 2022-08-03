import streamlit as st

st.set_page_config(
    page_title="About"
)
st.sidebar.header("About Page")
st.write("# About and How-To-Use")

st.markdown(
    """
    This project was created to use binary logistic regression to predict economic recessions using consumer
    commodities in the US.  The data was gathered from US entity databases including EIA and FRED.  At it's current
    state, the user can interact with pre-loaded data, the user can see the raw data as well as pre-set options for 
    cleaned data.  In-depth reporting can be seen at the bottom of pages with dataframe info, correlation, min, max,
    etc.
    
    ## To do
    - Integrate upload functionality to upload own data (must be in csv format).
    - Select options for which data to clean.
    -- Currently using interpolation for existing data, using average annual for months missing.
    -- Oil product prices marked as "Not Applicable" will be replaced with 0's rather than interpolation.
    --- This is because not applicable means products were not widely available at time (e.g. unleaded fuel)
    """
)