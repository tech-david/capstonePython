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
      - Provides information about application and its use
    ### Preloaded data
    - Navigate to 'DataExploration'
    """)
