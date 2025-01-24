import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    try:
        # Load the cleaned dataset
        data = pd.read_csv(r'C:\Users\ASUS\Desktop\Hackathon Project\data\Cleaned_Student_Performance_Factors_Cleaned.csv')
        
        # Scatter plot: Study Time vs. Grades
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x='study_time', y='grades', data=data)
        plt.title('Study Time vs. Grades')
        plt.xlabel('Study Time (hours)')
        plt.ylabel('Grades')
        plt.savefig(r'C:\Users\ASUS\Desktop\Hackathon Project\reports\study_time_vs_grades.png')
        plt.close()
        
        # Pie chart: Family Support Levels
        family_support_counts = data['family_support'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(family_support_counts, labels=family_support_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Family Support Levels')
        plt.savefig(r'C:\Users\ASUS\Desktop\Hackathon Project\reports\family_support_levels.png')
        plt.close()
        
        # Histogram: Distribution of Grades
        plt.figure(figsize=(10, 5))
        plt.hist(data['grades'], bins=30, alpha=0.7, color='blue')
        plt.title('Distribution of Grades')
        plt.xlabel('Grades')
        plt.ylabel('Frequency')
        plt.savefig(r'C:\Users\ASUS\Desktop\Hackathon Project\reports\grades_distribution.png')
        plt.close()
        
        print("Visualizations created successfully.")
        
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_visualizations()