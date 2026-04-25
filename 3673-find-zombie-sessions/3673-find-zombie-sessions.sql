# Write your MySQL query statement below


# fulfill all the criteria:
# duration > 30
# AND
# number of event_type = "scroll" >= 5
# AND
# number of event_type = "click" / number of event_type = "scroll" 
# AND
# number of event_type = "purchase" = 0


# combine all
SELECT
    session_id, 
    user_id, 
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes,
    SUM(event_type = 'scroll') AS scroll_count 
    #SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count

FROM app_events
GROUP BY user_id, session_id
HAVING
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30
    AND
    SUM(event_type = 'scroll') >= 5
    AND 
    SUM(event_type = 'click') / NULLIF(SUM(event_type = 'scroll'), 0) < 0.2
    AND
    SUM(event_type = 'purchase') = 0

ORDER BY scroll_count DESC, session_id
;

#能一起做的前提就是 grain 一樣
#全部都是 GROUP BY user_id, session_id，所以一個 GROUP BY + HAVING 就能全部解決
#grain 一樣 → 一個 query 搞定