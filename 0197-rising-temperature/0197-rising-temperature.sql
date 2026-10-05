# Write your MySQL query statement below
SELECT
    c.id
FROM Weather AS p
JOIN Weather AS c
ON DATEDIFF(c.recordDate, p.recordDate) = 1
and p.temperature < c.temperature
;