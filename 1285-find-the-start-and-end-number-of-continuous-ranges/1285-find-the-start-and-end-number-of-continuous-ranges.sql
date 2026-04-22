# Write your MySQL query statement below

# assign row number
WITH rank_id AS (
    SELECT 
        log_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS rk
    FROM Logs
),

# calculate log_id - rk to get the grouping key
create_key AS (
    SELECT 
        log_id,
        log_id - rk AS group_key
    FROM rank_id
)

#get min & max as start & end
SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM create_key
GROUP BY group_key
ORDER BY start_id;