-- Display all records

SELECT *
FROM employees;

--------------------------------------------------

-- Employees with Monthly Income greater than 5000

SELECT EmployeeNumber,
Department,
MonthlyIncome
FROM employees
WHERE MonthlyIncome > 5000;

--------------------------------------------------

-- Top 10 highest income employees

SELECT EmployeeNumber,
Department,
MonthlyIncome
FROM employees
ORDER BY MonthlyIncome DESC
LIMIT 10;

--------------------------------------------------

-- Count employees by department

SELECT Department,
COUNT(*) AS TotalEmployees
FROM employees
GROUP BY Department;

--------------------------------------------------

-- Average income by department

SELECT Department,
AVG(MonthlyIncome) AS AverageIncome
FROM employees
GROUP BY Department;

--------------------------------------------------

-- Minimum and maximum income by department

SELECT Department,
MIN(MonthlyIncome) AS MinIncome,
MAX(MonthlyIncome) AS MaxIncome
FROM employees
GROUP BY Department;

--------------------------------------------------

-- Employees who left the company

SELECT EmployeeNumber,
Department
FROM employees
WHERE Attrition='Yes';

--------------------------------------------------

-- Rank employees by Monthly Income

SELECT EmployeeNumber,
MonthlyIncome,
RANK() OVER(
ORDER BY MonthlyIncome DESC
) AS IncomeRank
FROM employees;

--------------------------------------------------

-- Running Total Income

SELECT EmployeeNumber,
Department,
MonthlyIncome,
SUM(MonthlyIncome)
OVER(
PARTITION BY Department
ORDER BY MonthlyIncome
) AS RunningTotal
FROM employees;