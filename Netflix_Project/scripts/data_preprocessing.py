import pandas as pd
import numpy as np  # Optional, only if you need specific numeric functions

def load_data(filepath):
    """
    Load data from a specified file path.
    
    Parameters:
    - filepath: str, path to the data file (e.g., .csv or .xlsx)
    
    Returns:
    - df: DataFrame, loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

def clean_data(df):
    """
    Clean the dataset by handling missing values and duplicates.
    
    Parameters:
    - df: DataFrame, the dataset to be cleaned
    
    Returns:
    - df: DataFrame, cleaned dataset
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values (you can adjust the method as needed)
    df = df.fillna(method='ffill')  # Example: forward filling missing values
    
    print("Data cleaned successfully.")
    return df
