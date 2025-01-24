def create_report():
    try:
        with open(r'C:\Users\ASUS\Desktop\Hackathon Project\reports\summary_report.txt', 'w') as f:
            f.write("Student Performance Analysis Report\n")
            f.write("=" * 50 + "\n")
            f.write("Key Findings:\n")
            f.write("1. There is a positive correlation between study time and grades.\n")
            f.write("2. Family support significantly influences student performance.\n")
            f.write("3. Students who participate in extracurricular activities tend to have better grades.\n")
            f.write("\nRecommendations:\n")
            f.write("1. Encourage students to allocate more study time to improve grades.\n")
            f.write("2. Implement programs to enhance family engagement in students' education.\n")
            f.write("3. Provide resources for students to balance extracurricular activities with academic responsibilities.\n")
            f.write("\nVisualizations:\n")
            f.write("1. Scatter plot of Study Time vs. Grades saved as 'study_time_vs_grades.png'.\n")
            f.write("2. Pie chart of Family Support Levels saved as 'family_support_levels.png'.\n")
            f.write("3. Histogram of Grades Distribution saved as 'grades_distribution.png'.\n")
            f.write("\nEnd of Report\n")
        
        print("Report generated successfully.")
        
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    create_report()