"""
Data Loader Module
Load S&P 500 Stock Prices dataset for Financial Intelligence Project
"""

import pandas as pd
import os
from pathlib import Path


def load_stock_data():
    """
    Load S&P 500 Stock Prices dataset from data/raw folder
    
    Returns:
    -------
    pd.DataFrame
        DataFrame containing S&P 500 stock prices (2014-2017)
        Columns: Date, Open, High, Low, Close, Volume, etc.
    
    Raises:
    ------
    FileNotFoundError
        If the CSV file is not found in the expected location
    """
    
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    file_path = project_root / 'data' / 'raw' / 'S&P 500 Stock Prices 2014-2017.csv'
    
    # Check if file exists
    if not file_path.exists():
        raise FileNotFoundError(
            f"Data file not found: {file_path}\n"
            f"Please ensure the S&P 500 Stock Prices CSV is in: data/raw/"
        )
    
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    return df


def preview_data():
    """
    Load and preview the first few rows of stock data
    
    Returns:
    -------
    pd.DataFrame
        First 5 rows of the stock prices dataset
    """
    df = load_stock_data()
    return df.head()


def get_data_info():
    """
    Get basic information about the stock prices dataset
    
    Returns:
    -------
    dict
        Dictionary containing dataset shape, columns, and data types
    """
    df = load_stock_data()
    
    info = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'date_range': {
            'start': df.iloc[0, 0] if len(df) > 0 else None,
            'end': df.iloc[-1, 0] if len(df) > 0 else None
        }
    }
    
    return info


# Example usage
if __name__ == "__main__":
    # Load the full dataset
    print("Loading S&P 500 Stock Prices dataset...")
    df = load_stock_data()
    
    # Preview the data
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Get dataset information
    print("\nDataset Information:")
    info = get_data_info()
    print(f"Shape: {info['shape']}")
    print(f"Columns: {info['columns']}")
    print(f"Data Types:\n{pd.Series(info['dtypes'])}")
    print(f"Missing Values:\n{pd.Series(info['missing_values'])}")
