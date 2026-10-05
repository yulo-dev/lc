# Write your MySQL query statement below

WITH rate AS (
    SELECT
        user_id, 
        ROUND(
            SUM(action = "confirmed") / COUNT(*)
            ,2) AS ratio
    FROM Confirmations
    GROUP BY user_id
)

SELECT s.user_id, COALESCE(r.ratio, 0.00) AS confirmation_rate
FROM Signups AS s LEFT JOIN rate AS r
ON s.user_id = r.user_id
;
