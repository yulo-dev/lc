# Write your MySQL query statement below


#DAYOFWEEK -> SUN ~ SAT:  1 ~ 7 
#WEEKDAY -> MON ~ SUN: 0 ~ 6
#WEEK() 


# use DAYOFWEEK to get the week day per day
# get the week_of_month GROUP BY WEEK(day)

WITH week_day AS (
    SELECT
        user_id, purchase_date, amount_spend,
        DAYOFWEEK(purchase_date) AS day_of_week,
        MOD(WEEK(purchase_date) , 4) + 1  AS week_of_month
    FROM Purchases
)

SELECT
    week_of_month, 
    purchase_date, 
    SUM(amount_spend) AS total_amount
FROM week_day
WHERE day_of_week = 6
GROUP BY week_of_month
ORDER BY week_of_month;


