# Write your MySQL query statement below

# find the first date, and check if lead(1) is the first date + 1
# numerator: # of players that logged in again after they first logged in
# denominator: # of player 


WITH login_after_first_date AS (
    SELECT 
        player_id, device_id, 
        event_date,
        LEAD(event_date, 1) OVER (PARTITION BY player_id ORDER BY event_date) AS event_next_date,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rk
    FROM Activity
)

SELECT
    ROUND(
        SUM(CASE WHEN DATEDIFF(event_next_date, event_date) = 1 THEN 1 ELSE 0 END) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity)
        , 2) AS fraction
FROM login_after_first_date
WHERE rk = 1;