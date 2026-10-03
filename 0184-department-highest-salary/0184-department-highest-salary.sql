# Write your MySQL query statement below

WITH ranking AS (
    SELECT
        name, departmentId, salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk 
    FROM Employee
)

SELECT 
    d.name AS Department, f.name AS Employee, f.salary
FROM Department AS d JOIN ranking AS f 
ON d.id = f.departmentId
WHERE f.rk = 1
; 

