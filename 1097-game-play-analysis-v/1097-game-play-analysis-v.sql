# Write your MySQL query statement below


# -- GOAL: output the day1_retention + number of installs per install_dt
# -- (1) get the first event_date as install date per player USING MIN + GROUP BY, 
# -- (1.1) count of player per install date as denominator (installs), count the player that has login the net day as numerator
# -- (2) count the Day1_retention by using numerator * 1.0 / denominator


# -- (1) get the first event_date as install date: MIN(date) is the first day per player
# grain: one row per player_id
WITH install AS (
    SELECT
        player_id, MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)

# grain: one row per install_dt
SELECT
    i.install_dt,
    COUNT(*) AS installs,
    #[注意！]這邊的numerator是抓a的 代表有合併到的(也就是有下一天的)才算入分子
    ROUND(
        COUNT(a.player_id) * 1.0 / COUNT(*)
    ,2) AS Day1_retention
FROM install AS i 
LEFT JOIN Activity AS a 
on i.player_id = a.player_id 
# [注意！]這邊是用AND 不是WHERE 所以就算沒有合併到的record也不會被排除掉 只是如果有合併到的 就要follow
AND DATEDIFF(a.event_date, i.install_dt) = 1
GROUP BY i.install_dt;