# Write your MySQL query statement below


# fulfill all the criteria:
# duration > 30
# AND
# number of event_type = "scroll" >= 5
# AND
# number of event_type = "click" / number of event_type = "scroll" 
# AND
# number of event_type = "purchase" = 0


# check the criteria one by one
# duration: For each user, use MAX OF event_timestamp - MIN OF event_timestamp to get the DURATION 
# grain: each row per user_id
# syntax: TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30

WITH duration_30 AS (
    SELECT 
        user_id, session_id, MAX(event_timestamp) AS max_event_timestamp, MIN(event_timestamp) AS min_event_timestamp
    FROM app_events
    GROUP BY user_id, session_id
    HAVING TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30
),

# number of event_type = "scroll" >= 5
# filter event_type = "scroll" then count(*) by grouping user_id and filter >= 5
# grain: one row per user_id

scroll_5 AS (
    SELECT
        user_id, session_id, COUNT(*) AS scroll_count
    FROM app_events
    WHERE event_type = 'scroll'
    GROUP BY user_id, session_id
    HAVING COUNT(*) >= 5
),

# number of event_type = "click" / number of event_type = "scroll" 
# filter event_type = "click" then count(*) by grouping user_id 
# filter event_type = "scroll" then count(*) by grouping user_id 
# grain: one row per user_id

count_click AS (
    SELECT
        user_id, session_id, COUNT(*) AS click_times
    FROM app_events
    WHERE event_type = 'click' 
    GROUP BY user_id, session_id
),
calculate_ratio AS (
    SELECT 
        s.user_id, s.session_id,
        ROUND(
            COALESCE(
            c.click_times * 1.0 / NULLIF(s.scroll_count, 0)
            ,0)
        ,2) AS ratio
    FROM scroll_5 AS s 
    LEFT JOIN count_click AS c
    ON s.user_id = c.user_id
),

# number of event_type = "purchase" = 0
have_purchase AS (
    SELECT 
        user_id, session_id
    FROM app_events
    WHERE event_type = 'purchase'
    GROUP BY user_id, session_id 
)

# combine all
SELECT
    d.session_id, d.user_id, TIMESTAMPDIFF(MINUTE, d.min_event_timestamp, d.max_event_timestamp) AS session_duration_minutes,
    s.scroll_count    
FROM duration_30 AS d

JOIN scroll_5 AS s
ON d.session_id = s.session_id AND d.user_id = s.user_id 

JOIN calculate_ratio AS c
ON d.session_id = c.session_id AND d.user_id = c.user_id  

LEFT JOIN have_purchase AS h
ON d.session_id = h.session_id AND d.user_id = h.user_id 

WHERE c.ratio < 0.20 AND h.user_id IS NULL
ORDER BY s.scroll_count DESC, d.session_id
;