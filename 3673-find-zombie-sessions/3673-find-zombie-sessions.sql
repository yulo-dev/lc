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