import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_analysis():
    try:
        # Load the cleaned dataset
        data = pd.read_csv(r'C:\Users\ASUS\Desktop\Hackathon Project\data\Cleaned_Student_Performance_Factors_Cleaned.csv')
        
        # Check unique values in the relevant columns
        print("Unique values in study_time:", data['study_time'].unique())
        print("Unique values in family_support:", data['family_support'].unique())
        print("Unique values in grades:", data['grades'].unique())

        # Convert categorical values to numeric
        mapping_study_time = {'low': 1, 'medium': 2, 'high': 3}
        mapping_family_support = {'low': 1, 'medium': 2, 'high': 3}

        data['study_time'] = data['study_time'].map(mapping_study_time)
        data['family_support'] = data['family_support'].map(mapping_family_support)

        # Convert grades to numeric
        data['grades'] = pd.to_numeric(data['grades'], errors='coerce')

        # Drop rows with NaN values
        data.dropna(inplace=True)

        # Calculate correlations
        correlation_matrix = data[['study_time', 'family_support', 'grades']].corr()
        print("Correlation matrix:")
        print(correlation_matrix)
        
        # Identify significant correlations
        study_time_grade_corr = correlation_matrix.loc['study_time', 'grades']
        family_support_grade_corr = correlation_matrix.loc['family_support', 'grades']
        
        print(f"Correlation between Study Time and Grades: {study_time_grade_corr}")
        print(f"Correlation between Family Support and Grades: {family_support_grade_corr}")

        # Visualize the correlation matrix
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    perform_analysis()