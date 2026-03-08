# Cancer Mortality Data Analysis (2018–2023)

## Overview
This project analyzes cancer mortality trends in the United States from **2018–2023**, focusing on **children and adolescents ages 1–19**. 

The purpose of this analysis is to explore mortality patterns among younger populations, which are a key focus of pediatric cancer research organizations such as **St. Jude Children's Research Hospital**.

Using publicly available data from the **CDC WONDER Cancer Mortality Database**, the project performs data cleaning, exploratory data analysis, and visualization to identify trends in cancer deaths and age-adjusted mortality rates among younger age groups.

The goal is to demonstrate a structured **data analysis workflow** while examining cancer mortality trends relevant to pediatric and adolescent populations.

## Objectives
Clean and preprocess raw public health data

Analyze year-to-year trends in cancer mortality

Compare death counts vs age-adjusted mortality rates

Create visualizations to identify patterns and changes over time

Demonstrate a reproducible data analysis pipeline

## Dataset
The dataset used in this project was obtained from the **CDC WONDER Cancer Mortality Database**.

Source:
https://wonder.cdc.gov/cancermort-v2022_SR.html

The data was manually filtered and exported as a CSV file using the CDC WONDER query interface before analysis.

### Query Configuration
The dataset was filtered using the following parameters in the CDC WONDER interface.

**Group Results By**
- Year

**Measures**
- Deaths
- Age-Adjusted Rates
- Crude Rates

**Location**
- United States

**Years Selected**
- 2018–2023

**Age Groups Selected**
- < 1 year
- 1–4 years
- 5–9 years
- 10–14 years
- 15–19 years

**Sex**
- All Sexes

**Race**
- All Races

**Ethnicity**
- All Ethnicities

**Export Format**
- CSV (Comma Separated Values)

## Project Workflow
### 1. Data Extraction
Cancer mortality data was generated and downloaded from the CDC WONDER database using custom query filters.

### 2. Data Cleaning
The dataset was processed using **Pandas** to:
- Remove unnecessary fields
- Ensure correct data types
- Prepare the dataset for analysis

### 3. Exploratory Data Analysis
Initial exploration was performed to understand patterns and changes in cancer mortality among children and adolescents.

### 4. Trend Analysis
Year-to-year changes were calculated to observe trends in mortality counts and rates.

### 5. Data Visualization
Visualizations were created to clearly communicate mortality trends over time.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Installation & Usage

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/shivaakg67/cancer-analysis.git
cd cancer-analysis
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

Mac / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install pandas matplotlib seaborn jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks in the **notebooks/** folder to reproduce the analysis.

## Author
Shivaa Karthikgavaskar  
Computer Science Student | University of Memphis
