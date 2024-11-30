import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Set the page configuration
# st.set_page_config(layout="wide")

def app():
    # Title
    st.title("Interactive Data Analysis App")

    # File uploader
    st.sidebar.header("Upload Your Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        # Load the dataset
        df = pd.read_csv(uploaded_file)
        st.header("Dataset Overview")
        st.write("### First 10 Rows of the Dataset")
        st.write(df.head(10))

        # Dataset Info
        st.write("### Dataset Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        # Dataset Statistics
        st.write("### Dataset Statistics")
        st.write(df.describe())

        # Data Visualization
        st.header("Data Visualizations")

        # # Correlation heatmap
        # st.write("### Correlation Heatmap")
        # fig, ax = plt.subplots(figsize=(10, 6))
        # sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        # st.pyplot(fig)

        # Histogram
        st.write("### Distribution of a Column")
        column = st.selectbox("Select a column for the histogram", df.select_dtypes(include=['float', 'int']).columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=20, kde=True, ax=ax)
        st.pyplot(fig)

        # Scatter plot
        st.write("### Scatter Plot")
        columns = df.select_dtypes(include=['float', 'int']).columns
        x_axis = st.selectbox("Select X-axis", columns)
        y_axis = st.selectbox("Select Y-axis", columns)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    else:
        st.warning("Please upload a CSV file to start the analysis.")
