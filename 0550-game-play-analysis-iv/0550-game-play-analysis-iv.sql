# Write your MySQL query statement below
WITH first_login AS (
    SELECT player_id, min(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(
        AVG(a.event_date IS NOT NULL)
    , 2) 
    AS fraction

FROM first_login AS f LEFT JOIN Activity AS a
ON f.player_id = a.player_id and datediff(a.event_date, f.first_login_date) = 1;