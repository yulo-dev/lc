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


# 如果要單獨算分母 要用 SELECT COUNT(DISTINCT player_id) FROM Activity
# 把所有 player_id 去重後數總數 → 一個數字，才能當分母。