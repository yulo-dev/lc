CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT 
        max(salary) AS getNthHighestSalary
      FROM (
        SELECT 
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS rk
        FROM Employee
      ) AS t
      WHERE rk = N
  );
END