import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib  # To load/save ML models

# Set the page configuration
# st.set_page_config(layout="wide")

# Load or train a machine learning model
@st.cache_resource
def load_model():
    # Dummy dataset (replace with your actual model and data)
    from sklearn.datasets import load_iris
    data = load_iris()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, X.columns

def app():
    st.title("Machine Learning Model Output App")

    # Sidebar for model options
    st.sidebar.header("Upload Data for Prediction")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    
    # Load the model
    model, feature_columns = load_model()

    if uploaded_file:
        # Load uploaded data
        user_data = pd.read_csv(uploaded_file)

        # Show the uploaded data
        st.subheader("Uploaded Data")
        st.write(user_data.head())

        # Check if required columns are present
        missing_cols = [col for col in feature_columns if col not in user_data.columns]
        if missing_cols:
            st.error(f"Missing required columns: {missing_cols}")
        else:
            # Make predictions
            predictions = model.predict(user_data[feature_columns])

            # Display predictions
            user_data["Predictions"] = predictions
            st.subheader("Prediction Results")
            st.write(user_data)

            # Optionally download results
            st.download_button(
                label="Download Predictions",
                data=user_data.to_csv(index=False),
                file_name="predictions.csv",
                mime="text/csv",
            )
    else:
        st.info("Please upload a iris dataset for prediction.")
