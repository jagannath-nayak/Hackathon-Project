import pandas as pd

def clean_dataset():
    try:
        # Load the dataset
        data = pd.read_csv(r'C:\Users\ASUS\Desktop\Hackathon Project\data\Cleaned_Student_Performance_Factors.csv')
        
        # Perform data cleaning operations
        # Example: Drop rows with missing values
        data.dropna(inplace=True)  # Adjust this based on your cleaning needs
        
        # Save the cleaned dataset
        data.to_csv(r'C:\Users\ASUS\Desktop\Hackathon Project\data\Cleaned_Student_Performance_Factors_Cleaned.csv', index=False)
        print("Data cleaning completed successfully.")
        
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clean_dataset()