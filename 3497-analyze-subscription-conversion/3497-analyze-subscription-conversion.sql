# Write your MySQL query statement below


# Find users who converted from free trial to paid subscription
# Calculate each user's average daily activity duration during their free trial period (rounded to 2 decimal places)
# Calculate each user's average daily activity duration during their paid subscription period (rounded to 2 decimal places)

# calculate the avg_duration for free_trial & paid -> grain: one row per user per activity_type 
# filter the user that has both activity_type in free_trial & paid -> grain: one row per user 

WITH avg_duration AS (
    SELECT
        user_id, activity_type, 
        ROUND(
            AVG(activity_duration)
        , 2) AS avg_duration
    FROM UserActivity
    WHERE activity_type in ('free_trial', 'paid') 
    GROUP BY user_id, activity_type
)

SELECT
    f.user_id, f.avg_duration AS trial_avg_duration, p.avg_duration AS paid_avg_duration
FROM avg_duration AS f
JOIN avg_duration AS p
ON f.user_id = p.user_id
WHERE f.activity_type = 'free_trial' AND p.activity_type = 'paid'
ORDER BY user_id;