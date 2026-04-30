# Write your MySQL query statement below

# within 7 days: DATEDIFF(second purchase date, first purchase date) <= 7

# -- (1) get the second purchase date using LEAD(created_at) OVER (PARTITION BY user_id ORDER BY created_at) as next_created_at
WITH next_purchase AS (
    SELECT
        user_id, created_at, 
        LEAD(created_at) OVER (PARTITION BY user_id ORDER BY created_at) as next_created_at
    FROM Users
)
# -- (2) select distinct user_id where DATEDIFF(second purchase date, first purchase date) <= 7
SELECT
    DISTINCT user_id
FROM next_purchase
WHERE DATEDIFF(next_created_at, created_at) BETWEEN 0 AND 7;