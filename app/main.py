import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.title("Exploratory Data Analysis Dashboard")

# Sidebar for file upload and user inputs
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load the dataset
    data = pd.read_csv(uploaded_file)
    
    # Display dataset overview
    st.subheader("Dataset Overview")
    st.write("Shape of the dataset:", data.shape)
    st.write(data.head())

    # Dataset statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())

    # Column selection
    st.sidebar.subheader("Select Columns for Analysis")
    numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
    selected_columns = st.sidebar.multiselect("Select Numeric Columns", numeric_columns)

    # Visualization: Histograms
    if selected_columns:
        st.subheader("Histograms")
        for col in selected_columns:
            st.write(f"Histogram for {col}")
            fig, ax = plt.subplots()
            sns.histplot(data[col], kde=True, bins=30, color="blue", ax=ax)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            st.pyplot(fig)

    # Visualization: Correlation Heatmap
    st.subheader("Correlation Heatmap")
    if st.checkbox("Show Correlation Heatmap"):
        corr_matrix = data.corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        plt.title("Correlation Matrix")
        st.pyplot(fig)

    # Scatterplot for relationship analysis
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("Choose X-axis", options=numeric_columns)
    y_axis = st.selectbox("Choose Y-axis", options=numeric_columns)
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
        plt.title(f"{x_axis} vs {y_axis}")
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot(fig)

    # Display missing values
    st.subheader("Missing Values")
    missing_values = data.isnull().sum()
    st.write(missing_values[missing_values > 0])
else:
    st.write("Please upload a CSV file to proceed.")
