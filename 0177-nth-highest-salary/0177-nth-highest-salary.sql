CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH rank_employee AS (
        SELECT 
            salary,
            DENSE_RANK() OVER (ORDER BY salary desc) AS rk
        FROM Employee
      )
      SELECT 
        max(salary) AS getNthHighestSalary
      FROM rank_employee WHERE rk = N

  );
END