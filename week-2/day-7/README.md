# Week 2 - Day 7

## Advanced Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Graphics-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-007ACC)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-181717)

---

### Objective

The purpose of Day 7 was to perform a comprehensive Exploratory Data Analysis (EDA) on the IBM HR Analytics Employee Attrition dataset. The analysis focused on missing value analysis, outlier detection, distribution analysis, target variable analysis, and correlation analysis to better understand employee behavior and workforce trends.

---

## Folder Structure

```text
day-7/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── notebooks/
│   └── advanced_eda.ipynb
│
└── README.md
```

---

## Dataset Used

### IBM HR Analytics Employee Attrition & Performance Dataset

The IBM HR Analytics dataset contains employee demographic information, job-related attributes, salary details, and attrition records.

The dataset includes information such as:

* Employee Age
* Department
* Monthly Income
* Job Role
* Attrition Status
* Education Level
* Business Travel
* Job Satisfaction
* Work Experience

---

## EDA Tasks Performed

### 1. Dataset Overview

Basic information about the dataset was explored, including:

* Dataset Shape
* Column Names
* Data Types
* Statistical Summary

**Insights:**

* The dataset contains both numerical and categorical variables.
* Employee demographic and organizational information is available.

---

### 2. Missing Value Analysis

Data quality checks were performed to identify:

* Missing Values
* Missing Value Percentages

**Insights:**

* The dataset contains minimal or no missing values.
* Data quality is suitable for analysis.

---

### 3. Outlier Detection

Outliers were identified using:

* Boxplots
* IQR Method

**Insights:**

* Monthly Income contains several outliers.
* High-income employees contribute to extreme values.

---

### 4. Distribution Analysis

Histograms were created for:

* Employee Age
* Monthly Income

**Insights:**

* Most employees belong to middle-age groups.
* Monthly Income distribution is right-skewed.

---

### 5. Target Variable Analysis

The Attrition variable was analyzed.

**Insights:**

* Employee retention is significantly higher than attrition.
* Attrition cases represent a smaller portion of the workforce.

---

### 6. Correlation Analysis

A correlation heatmap was generated.

**Insights:**

* Several numerical variables show moderate positive correlations.
* Correlation analysis helps identify important features for future machine learning tasks.

---

## Key Findings

* Most employees belong to middle-age groups.
* Monthly Income contains several outliers.
* Employee retention is higher than attrition.
* Correlation analysis revealed relationships among employee features.
* The dataset is clean and suitable for machine learning.

---

## Concepts Practiced

### Pandas

* Data Loading
* Data Inspection
* Missing Value Analysis
* Statistical Analysis

### Data Visualization

* Histograms
* Boxplots
* Countplots
* Heatmaps

### Data Analysis

* Exploratory Data Analysis (EDA)
* Distribution Analysis
* Outlier Detection
* Correlation Analysis
* Target Variable Analysis

---

## Learning Outcomes

By completing Day 7, I learned how to:

* Perform advanced exploratory data analysis.
* Analyze missing values and data quality.
* Detect outliers using statistical methods.
* Study feature distributions.
* Analyze target variables.
* Interpret correlation heatmaps.
* Extract meaningful business insights from employee data.

---

## Tools Used

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Visual Studio Code (VS Code)
* Git
* GitHub
