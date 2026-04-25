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
)

SELECT
    ROUND(
        COALESCE(
            count(*) * 1.0 
            / 
            NULLIF(
                COUNT(DISTINCT user_id)
                ,0)
        ,0)
    ,2) AS average_sessions_per_user
FROM within_window;