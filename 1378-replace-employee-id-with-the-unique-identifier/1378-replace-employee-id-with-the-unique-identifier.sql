# Write your MySQL query statement below
SELECT b.unique_id, a.name
FROM Employees as a left join EmployeeUNI as b ON a.id = b.id;