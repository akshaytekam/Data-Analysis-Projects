import pandas as pd
import streamlit as st

import page1
import page2
import page3
import page4
import page5
import page6

# Dictionary of pages
PAGES = {
    "Data Analysis": page5,
    "Machine Learning Model": page6,
    "Matplotlib": page1,
    "Seaborn": page2,
    "Plotly": page3,
    "Image Processing": page4
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    # Load the selected page
    page_select = PAGES[selection]
    page_select.app()

    

if __name__ == "__main__":
    main()