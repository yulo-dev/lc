# Write your MySQL query statement below

WITH ranking_table AS (
    SELECT
    salary, 
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rn
    FROM Employee
)

SELECT MAX(salary) AS SecondHighestSalary FROM ranking_table WHERE rn = 2;