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
    
    ## Features 
    ### Data Exploration
    Some of the current built-in features include being able to select columns for dataframe view.  As 
    well as being able to select the columns to use as X and Y axes for the graphs.  Suggested use is to use the 
    'Year' column as the X-axis and the price category as the Y-axis.  The prices are separated by months, 
    the cleaned data uses numbers instead of strings to indicate the month, and are equivalent to each other.
    ### Raw Vs Processed
    The page DataExploration will have the raw data prior to any cleaning.  The page ProcessedDataExploration will
    have the same functionality for processed data.  
    ### Reporting
    For more in-depth reporting, refer to the interactive reports in ElectricityReports, NaturalGasReports, 
    and Oil Reports. Please allow this section to render as it is resource intensive, you will see a spinner 
    indicating the application is loading the information. The report generation consists of cleaned data, 
    and does not include columns deemed irrelevant (e.g. Day column). You can also download the data as HTML using 
    download button located at the bottom of each corresponding report. 
    
    ## To do
    * Integrate upload functionality to upload own data (must be in csv format).
    * Select options for which data to clean.
      - Currently using interpolation for existing data, using average annual for months missing.
    """
)
