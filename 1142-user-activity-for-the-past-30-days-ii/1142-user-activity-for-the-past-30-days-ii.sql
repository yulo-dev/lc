# Write your MySQL query statement below

#activity table: might have duplicate
#goal: average number of sesion for each user in 30-day period ending on 2019-07-27 

# filter activity_date that is within previous 30 days before 2019-07-27 (DATEDIFF('2019-07-27', activity_date) <= 30)
# count the number of unique session_id for each user_id 
# numerator: sum the count   
# denominator: unique user_id 


WITH within_window AS (
    SELECT 
        DISTINCT user_id, session_id
    FROM Activity 
    WHERE DATEDIFF('2019-07-27', activity_date) <= 29
),

count_numerator AS (
    SELECT 
        COUNT(*) AS numerator
    FROM within_window
    GROUP BY user_id, session_id
)

SELECT
    ROUND(
        COALESCE(
            SUM(numerator) * 1.0 
            / 
            NULLIF(
                (SELECT COUNT(DISTINCT user_id) FROM within_window)
                ,0)
        ,0)
    ,2) AS average_sessions_per_user
FROM count_numerator; 