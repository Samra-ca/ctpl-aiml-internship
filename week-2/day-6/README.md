# Week 2 - Day 6

## SQL Fundamentals

![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1)
![SQL](https://img.shields.io/badge/SQL-Queries-orange)
![Database](https://img.shields.io/badge/Database-Management-blue)
![MySQL Workbench](https://img.shields.io/badge/MySQL_Workbench-Tool-00758F)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-181717)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-007ACC)

---

### Objective

The purpose of Day 6 was to learn and practice SQL fundamentals using a real-world HR Analytics dataset. The task involved importing data into MySQL, writing SQL queries, performing data filtering, sorting, aggregation, grouping, and applying window functions to extract meaningful insights from employee data.

---

## Folder Structure

```text
day-6/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── sql_queries.sql
│
├── sql_queries_summary.md
│
└── README.md
```

---

## Dataset Used

### IBM HR Analytics Employee Attrition & Performance Dataset

The IBM HR Analytics dataset was used to practice SQL operations and perform employee data analysis.

The dataset contains information such as:

* Employee Age
* Department
* Monthly Income
* Job Role
* Attrition Status
* Education Level
* Business Travel
* Job Satisfaction
* Work Experience

The dataset was analyzed using SQL queries to understand employee demographics, salary distribution, and workforce trends.

---

## SQL Tasks Performed

### 1. Data Retrieval

Basic SQL queries were used to retrieve employee records.

**Queries Used:**

* SELECT *
* SELECT specific columns

**Insights:**

* Successfully viewed employee information.
* Explored available dataset attributes.

---

### 2. Data Filtering

The WHERE clause was used to filter employee records based on conditions.

**Queries Used:**

* Employees with Monthly Income greater than 5000
* Employees with Attrition = 'Yes'

**Insights:**

* Identified high-income employees.
* Analyzed employees who left the organization.

---

### 3. Data Sorting

ORDER BY was used to sort records.

**Queries Used:**

* Highest Monthly Income employees

**Insights:**

* Identified top earners in the organization.
* Observed salary distribution patterns.

---

### 4. Aggregate Analysis

Aggregate functions were used to summarize employee data.

**Functions Used:**

* COUNT()
* AVG()
* MIN()
* MAX()

**Insights:**

* Calculated employee count by department.
* Found average departmental income.
* Identified minimum and maximum salaries.

---

### 5. GROUP BY Analysis

GROUP BY was used to perform department-level analysis.

**Insights:**

* Compared employee distribution across departments.
* Analyzed salary statistics department-wise.

---

### 6. Window Functions

Advanced SQL analytical functions were applied.

**Functions Used:**

* RANK()
* SUM() OVER()

**Insights:**

* Ranked employees based on Monthly Income.
* Calculated running totals of departmental salaries.

---

## SQL Concepts Practiced

### SQL Fundamentals

* SELECT
* WHERE
* ORDER BY
* LIMIT
* GROUP BY

### Aggregate Functions

* COUNT()
* AVG()
* MIN()
* MAX()

### Window Functions

* RANK()
* SUM() OVER()

### Data Analysis

* Employee Analysis
* Salary Analysis
* Department Analysis
* Workforce Insights

---

## Key Findings

* Research & Development and Sales contain the highest number of employees.
* Employee salaries vary significantly across departments.
* High-income employees can be easily identified using ranking functions.
* Department-wise analysis provides useful workforce insights.
* SQL helps efficiently retrieve and analyze business data.

---

## Learning Outcomes

By completing Day 6, I learned how to:

* Import CSV datasets into MySQL.
* Write SQL queries for data retrieval and analysis.
* Filter and sort records using SQL.
* Perform aggregation and grouping operations.
* Apply window functions for advanced analysis.
* Generate business insights from relational data.
* Organize SQL projects professionally using GitHub.

---

## Tools Used

* MySQL
* MySQL Workbench
* SQL
* Git
* GitHub
* Visual Studio Code (VS Code)
