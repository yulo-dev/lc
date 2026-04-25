# Write your MySQL query statement below

WITH rank_salary AS (
    SELECT
        id, name, salary, departmentId,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk
    FROM Employee
)

SELECT 
    d.name AS Department, 
    r.name AS Employee, 
    r.salary AS Salary
FROM rank_salary AS r 
JOIN Department AS d
ON r.departmentId = d.id
WHERE r.rk <= 3
ORDER BY d.name, r.salary;