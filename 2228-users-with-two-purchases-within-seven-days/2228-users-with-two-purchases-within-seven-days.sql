# Write your MySQL query statement below


# LAG(purchase_date) OVER (PARTITION BY user_id ORDER BY purchase_date) AS prev_purchase_date
# check the DATE_DIFF(purchase_date, prev_purchase_date) BETWEEN 0 AND 6
# dedup user_id

WITH get_previous AS (
    SELECT 
        purchase_id, user_id, purchase_date,
        LAG(purchase_date) OVER (PARTITION BY user_id ORDER BY purchase_date) AS prev_purchase_date
    FROM Purchases
)

SELECT
    DISTINCT user_id
FROM get_previous
WHERE DATEDIFF(purchase_date, prev_purchase_date) BETWEEN 0 AND 7;