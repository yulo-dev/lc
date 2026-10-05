# Write your MySQL query statement below

WITH activity_join AS (
    SELECT 
        a.machine_id, a.process_id, e.timestamp - a.timestamp as time_diff
    FROM Activity AS a JOIN Activity AS e
    ON a.machine_id = e.machine_id AND a.process_id = e.process_id
    WHERE a.activity_type = 'start' AND e.activity_type = 'end' 
)

SELECT
    machine_id,
    ROUND(
        COALESCE(
            SUM(time_diff) / NULLIF(COUNT(*), 0),0)
        ,3) AS processing_time

FROM activity_join
GROUP BY machine_id
;