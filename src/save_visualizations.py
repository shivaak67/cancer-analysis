#!/usr/bin/env python3
"""
Script to save all visualization plots from notebooks to outputs/figures directory.
This script extracts and saves the plots generated in the analysis notebooks.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import sys
import os

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Set up paths
OUTPUTS_DIR = project_root / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
DATA_DIR = project_root / "data"
PROCESSED_DIR = DATA_DIR / "processed"

# Create directories if they don't exist
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    """Load the cleaned cancer data."""
    data_file = PROCESSED_DIR / "cleaned_cancer_data.csv"
    if not data_file.exists():
        raise FileNotFoundError(f"Cleaned data file not found: {data_file}")
    
    df = pd.read_csv(data_file)
    df_sorted = df.sort_values('Year')
    return df_sorted

def save_time_series_trends(df_sorted):
    """Save time series trend visualization."""
    print("Generating Time Series Trend Visualization...")
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Cancer Mortality Time Series Trends (2018-2023)', fontsize=16, fontweight='bold')
    
    # 1. Deaths Trend
    axes[0, 0].plot(df_sorted['Year'], df_sorted['Deaths'], 'o-', linewidth=3, markersize=8, color='#e74c3c')
    axes[0, 0].set_title('Total Deaths Over Time', fontweight='bold')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Number of Deaths')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].ticklabel_format(style='plain', axis='y')
    axes[0, 0].axvline(x=2020, color='gray', linestyle='--', alpha=0.7, label='Trend Reversal')
    axes[0, 0].legend()
    
    # 2. Population Trend
    axes[0, 1].plot(df_sorted['Year'], df_sorted['Population'], 's-', linewidth=3, markersize=8, color='#3498db')
    axes[0, 1].set_title('Population Over Time', fontweight='bold')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Population')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].ticklabel_format(style='plain', axis='y')
    
    # 3. Age-Adjusted vs Crude Rate Comparison
    axes[1, 0].plot(df_sorted['Year'], df_sorted['Age-Adjusted Rate'], '^-', linewidth=3, markersize=8, color='#27ae60', label='Age-Adjusted Rate')
    axes[1, 0].plot(df_sorted['Year'], df_sorted['Crude Rate'], 'v-', linewidth=3, markersize=8, color='#f39c12', label='Crude Rate')
    axes[1, 0].set_title('Mortality Rates Comparison', fontweight='bold')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].set_ylabel('Rate per 100,000')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    axes[1, 0].axvline(x=2020, color='gray', linestyle='--', alpha=0.7)
    
    # 4. Deaths vs Population (Dual Axis)
    ax4_twin = axes[1, 1].twinx()
    line1 = axes[1, 1].plot(df_sorted['Year'], df_sorted['Deaths'], 'o-', linewidth=3, markersize=8, color='#e74c3c', label='Deaths')
    line2 = ax4_twin.plot(df_sorted['Year'], df_sorted['Population'], 's-', linewidth=3, markersize=8, color='#3498db', label='Population')
    axes[1, 1].set_title('Deaths vs Population (Opposing Trends)', fontweight='bold')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Number of Deaths', color='#e74c3c')
    ax4_twin.set_ylabel('Population', color='#3498db')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].tick_params(axis='y', labelcolor='#e74c3c')
    ax4_twin.tick_params(axis='y', labelcolor='#3498db')
    
    # Add legends for dual axis
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    axes[1, 1].legend(lines, labels, loc='upper left')
    
    plt.tight_layout()
    
    # Save the figure
    output_file = FIGURES_DIR / "01_time_series_trends.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_file}")

def save_correlation_heatmap(df_sorted):
    """Save correlation heatmap visualization."""
    print("Generating Correlation Heatmap...")
    
    # Calculate correlation matrix
    corr_matrix = df_sorted[['Deaths', 'Population', 'Age-Adjusted Rate', 'Crude Rate']].corr()
    
    # Create correlation heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                square=True,
                linewidths=0.5,
                cbar_kws={"shrink": .8},
                fmt='.3f',
                annot_kws={'size': 14, 'weight': 'bold'})
    
    plt.title('Cancer Mortality Correlation Matrix\n(2018-2023)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)
    plt.tight_layout()
    
    # Save the figure
    output_file = FIGURES_DIR / "02_correlation_heatmap.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_file}")

def main():
    """Main function to generate and save all visualizations."""
    print("=" * 60)
    print("CANCER ANALYSIS - VISUALIZATION GENERATOR")
    print("=" * 60)
    
    try:
        # Load data
        print("Loading cleaned data...")
        df_sorted = load_data()
        print(f"Data loaded: {df_sorted.shape[0]} rows × {df_sorted.shape[1]} columns")
        print(f"Years: {df_sorted['Year'].min()} - {df_sorted['Year'].max()}")
        print()
        
        # Generate all visualizations
        save_time_series_trends(df_sorted)
        save_correlation_heatmap(df_sorted)
        
        print("\n" + "=" * 60)
        print(f"All visualizations saved to: {FIGURES_DIR}")
        print("Generated files:")
        for file in sorted(FIGURES_DIR.glob("*.png")):
            print(f"  - {file.name}")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
