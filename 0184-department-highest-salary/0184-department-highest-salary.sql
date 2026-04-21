# Write your MySQL query statement below

# goal: find the emplyee(s) with highest salary in each department
# tie -> return all employees
# one department may have multiple rows

WITH rank_salary AS (
    # -- rank employee by salary within each department
    SELECT
        name,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk,
        departmentId
    FROM Employee
)

# filter rk = 1 to filter the tied heighest-salary employees in each department
# join Department to return Department name
SELECT 
    d.name AS Department,
    r.name AS Employee,
    r.salary

FROM rank_salary AS r JOIN Department AS d
ON r.departmentId = d.id
WHERE r.rk = 1;