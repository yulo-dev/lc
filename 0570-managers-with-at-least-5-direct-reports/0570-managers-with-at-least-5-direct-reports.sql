# Write your MySQL query statement below

#step1: only count the number
WITH manager_counts AS (
    SELECT managerId, COUNT(*) as report_count
    FROM Employee 
    GROUP BY managerId
)

#step2: get the name
SELECT e.name
FROM Employee AS e JOIN manager_counts AS m
ON e.id = m.managerId
WHERE report_count >= 5;

#嘗試用cte
#join=inner join