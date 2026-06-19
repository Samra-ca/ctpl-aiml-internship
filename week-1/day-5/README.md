# Week 1 - Day 5

## Mini Exploratory Data Analysis (EDA)

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

The purpose of Day 5 was to perform a complete Exploratory Data Analysis (EDA) on the Customer Personality Analysis dataset. The project involved data loading, inspection, cleaning, statistical analysis, and visualization to uncover meaningful patterns and insights. EDA is an important step in the data science workflow because it helps understand the dataset before applying machine learning techniques.

---

## Folder Structure

```text
day-5/
│
├── data/
│   └── marketing_campaign.csv
│
├── notebooks/
│   └── customer_eda.ipynb
│
└── README.md
```

---

## Dataset Used

### Customer Personality Analysis Dataset

The Customer Personality Analysis dataset was used to perform exploratory data analysis and visualization. The dataset contains customer demographic information, purchasing behavior, and campaign response details.

The dataset includes information such as:

* Customer Income
* Education Level
* Marital Status
* Birth Year
* Product Spending
* Campaign Responses
* Purchase Behavior

The dataset was analyzed to understand customer characteristics and spending patterns.

---

## EDA Tasks Performed

### 1. Dataset Overview

Basic information about the dataset was explored, including:

* Dataset Shape
* Column Names
* Data Types
* Sample Records

**Insights:**

* The dataset contains both numerical and categorical variables.
* Customer demographic and purchasing information is available.

---

### 2. Data Quality Assessment

Data quality checks were performed to identify:

* Missing Values
* Duplicate Records
* Incorrect Data Types

**Insights:**

* Missing values were found in the Income column.
* Duplicate records were identified and removed.

---

### 3. Data Cleaning

The following preprocessing steps were applied:

* Missing values were replaced using median values.
* Duplicate rows were removed.
* A new Age column was created using Year_Birth.

**Insights:**

* Data quality significantly improved after cleaning.
* The dataset became ready for analysis and visualization.

---

## Visualizations Created

### 1. Histogram

Used to visualize the distribution of customer ages.

**Insights:**

* Most customers belong to the middle-age group.
* Customer ages are concentrated within a specific range.

---

### 2. Bar Chart

Used to visualize the distribution of education levels.

**Insights:**

* Graduation and PhD are the most common education categories.
* Education levels vary across customers.

---

### 3. Box Plot

Used to analyze income distribution across education levels.

**Insights:**

* Customers with higher educational qualifications generally have higher incomes.
* Income values contain some outliers.

---

### 4. Correlation Heatmap

Used to identify relationships between numerical variables.

**Insights:**

* Positive relationships exist between income and spending variables.
* Heatmaps help identify important features for future machine learning tasks.

---

### 5. Scatter Plot

Used to analyze the relationship between customer income and wine spending.

**Insights:**

* Customers with higher incomes tend to spend more on wine products.
* A positive relationship exists between income and spending behavior.

---

### 6. Violin Plot

Used to compare income distribution across marital status groups.

**Insights:**

* Income distribution varies among different marital status categories.
* Marital status may influence purchasing behavior.

---

## Key Findings

* Most customers belong to the middle-age group.
* Graduation is the most common education level.
* Higher-income customers spend more on wine products.
* Income distribution varies across marital status groups.
* Data cleaning improved dataset quality and reliability.

---

## Concepts Practiced

### Pandas

* Data Loading
* Data Cleaning
* Missing Value Handling
* Duplicate Removal
* Statistical Analysis

### Data Visualization

* Histograms
* Bar Charts
* Box Plots
* Heatmaps
* Scatter Plots
* Violin Plots

### Data Analysis

* Exploratory Data Analysis (EDA)
* Distribution Analysis
* Correlation Analysis
* Pattern Recognition
* Insight Generation

---

## Learning Outcomes

By completing Day 5, I learned how to:

* Perform complete Exploratory Data Analysis (EDA).
* Inspect and clean real-world datasets.
* Handle missing values and duplicate records.
* Create meaningful visualizations.
* Interpret data patterns and relationships.
* Extract business insights from data.
* Present findings in a structured and professional manner.

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
