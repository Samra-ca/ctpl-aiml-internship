# Week 2 - Day 8

## Feature Engineering & Data Preprocessing

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-007ACC)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-181717)

---

### Objective

The purpose of Day 8 was to prepare the IBM HR Analytics dataset for machine learning by applying feature engineering and data preprocessing techniques. The task focused on improving data quality, transforming categorical variables, scaling numerical features, and creating new features to enhance model performance.

---

## Folder Structure

```text
day-8/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── notebooks/
│   └── feature_engineering.ipynb
│
└── README.md
```

---

## Dataset Used

### IBM HR Analytics Employee Attrition & Performance Dataset

The dataset contains employee demographic, salary, education, job satisfaction, and attrition information.

The dataset was preprocessed to make it suitable for machine learning model development.

---

## Tasks Performed

### 1. Data Loading

The dataset was loaded using Pandas.

**Insights:**

* Successfully imported employee data.
* Verified dataset structure and contents.

---

### 2. Missing Value Handling

The dataset was checked for missing values.

**Insights:**

* The dataset contains minimal missing values.
* No major imputation was required.

---

### 3. Feature Engineering

A new feature was created:

* ExperienceRatio

Formula:

```python
ExperienceRatio = TotalWorkingYears / Age
```

**Insights:**

* The new feature provides additional information about employee experience relative to age.

---

### 4. Categorical Feature Encoding

Categorical variables were converted into numerical values using Label Encoding.

Examples:

* Attrition
* BusinessTravel
* Department
* EducationField
* JobRole

**Insights:**

* Machine learning algorithms require numerical input.
* Encoding converts categorical information into usable numerical form.

---

### 5. Feature Scaling

Numerical variables were standardized using StandardScaler.

**Insights:**

* Features now have comparable scales.
* Scaling improves machine learning model performance.

---

## Key Findings

* The dataset required minimal cleaning.
* Feature engineering improved data representation.
* Categorical variables were successfully encoded.
* Numerical features were standardized.
* The dataset is now ready for machine learning model development.

---

## Concepts Practiced

### Data Preprocessing

* Missing Value Analysis
* Data Cleaning
* Feature Transformation

### Feature Engineering

* Derived Feature Creation
* Experience-Based Feature Development

### Machine Learning Preparation

* Label Encoding
* Feature Scaling
* Data Transformation

---

## Learning Outcomes

By completing Day 8, I learned how to:

* Prepare datasets for machine learning.
* Create meaningful engineered features.
* Encode categorical variables.
* Standardize numerical variables.
* Improve dataset quality and usability.
* Apply preprocessing techniques used in real-world AI projects.

---

## Tools Used

* Python 3.12
* Pandas
* NumPy
* Scikit-Learn
* Jupyter Notebook
* Visual Studio Code (VS Code)
* Git
* GitHub
