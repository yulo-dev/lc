# Write your MySQL query statement below

WITH cnt_manager AS (
    SELECT
        managerId, 
        COUNT(*) AS freq
    FROM Employee
    GROUP BY managerId
    HAVING freq >= 5
)

SELECT
    e.name
FROM Employee AS e JOIN cnt_manager AS c 
ON e.id = c.managerId
;

