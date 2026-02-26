"""
Data cleaning script for cancer mortality data.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def clean_cancer_data():
    """Clean the raw cancer mortality data and save processed version."""
    
    # Set up paths
    PROJECT_ROOT = Path(__file__).parent.parent
    RAW_DIR = PROJECT_ROOT / "data" / "raw"
    PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
    
    # Ensure processed directory exists
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load raw data
    raw_files = list(RAW_DIR.glob("*.csv"))
    if not raw_files:
        raise FileNotFoundError("No CSV files found in raw data directory")
    
    print(f"Loading raw data: {raw_files[0].name}")
    df = pd.read_csv(raw_files[0], low_memory=False)
    print(f"Original shape: {df.shape}")
    
    # Clean the data
    print("Cleaning data...")
    
    # Remove rows with all NaN values
    df_clean = df.dropna(how='all')
    print(f"After removing empty rows: {df_clean.shape}")
    
    # Keep only rows with valid years (removes metadata)
    df_clean = df_clean[df_clean['Year'].notna()]
    print(f"After filtering for valid years: {df_clean.shape}")
    
    # Convert data types
    for col in ['Year', 'Year Code', 'Deaths', 'Population']:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    for col in ['Age-Adjusted Rate', 'Crude Rate']:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # Remove any remaining rows with missing critical data
    df_clean = df_clean.dropna(subset=['Year', 'Deaths', 'Population'])
    print(f"After removing rows with missing critical data: {df_clean.shape}")
    
    # Reset index
    df_clean = df_clean.reset_index(drop=True)
    
    # Remove empty Notes column
    if 'Notes' in df_clean.columns:
        df_clean = df_clean.drop('Notes', axis=1)
        print("Removed empty Notes column")
    
    # Save cleaned data
    output_file = PROCESSED_DIR / "cleaned_cancer_data.csv"
    df_clean.to_csv(output_file, index=False)
    
    print(f"Cleaned data saved to: {output_file}")
    print(f"Final shape: {df_clean.shape}")
    print(f"Columns: {list(df_clean.columns)}")
    
    # Show sample of cleaned data
    print("\nSample of cleaned data:")
    print(df_clean.head())
    
    return df_clean

if __name__ == "__main__":
    clean_cancer_data()