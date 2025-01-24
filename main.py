import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import functions from other scripts
from src.data_cleaning import clean_dataset
from src.data_analysis import perform_analysis
from src.visualizations import create_visualizations
from src.report_generation import create_report

# Function to run Streamlit app
def run_streamlit_app():
    # Load cleaned dataset
    data = pd.read_csv('data/Cleaned_Student_Performance_Factors.csv')
    
    # Streamlit app title
    st.title("Student Performance Analysis")

    # Sidebar for user input
    st.sidebar.header("Select Visualization Type")
    visualization_type = st.sidebar.selectbox("Choose a visualization type", 
                                                ["Histogram", "Scatter Plot", "Pie Chart"])

    if visualization_type == "Histogram":
        column = st.sidebar.selectbox("Select a column for histogram", data.columns)
        if st.sidebar.button("Show Histogram"):
            plt.figure(figsize=(10, 6))
            sns.histplot(data[column], bins=30, kde=True)
            plt.title(f'Histogram of {column}')
            st.pyplot(plt)

    elif visualization_type == "Scatter Plot":
        x_column = st.sidebar.selectbox("Select X-axis column", data.columns)
        y_column = st.sidebar.selectbox("Select Y-axis column", data.columns)
        if st.sidebar.button("Show Scatter Plot"):
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=data, x=x_column, y=y_column)
            plt.title(f'Scatter Plot of {x_column} vs {y_column}')
            st.pyplot(plt)


    elif visualization_type == "Pie Chart":
        column = st.sidebar.selectbox("Select a column for pie chart", data.columns)
        if st.sidebar.button("Show Pie Chart"):
            plt.figure(figsize=(10, 6))
            data[column].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title(f'Pie Chart of {column}')
            st.pyplot(plt)

# Main function to orchestrate the workflow
def main():
    # Clean the dataset
    clean_dataset()  # Call the cleaning function from data_cleaning.py

    # Generate report
    create_report()  # Call the report generation function from report_generation.py

    # Run the Streamlit app
    run_streamlit_app()

# Execute the main function
if __name__ == "__main__":
    main()