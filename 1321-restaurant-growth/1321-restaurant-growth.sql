# Write your MySQL query statement below

#aggregate the total amount to one row per visit_on
#row-based window to calculate total amount over current visit and the previous 6 days

WITH aggregate_amount AS (
    SELECT
        visited_on, SUM(amount) AS amount_per_day
    FROM Customer
    GROUP BY visited_on
),
seven_day_amount AS (
    SELECT 
        visited_on,
        SUM(amount_per_day) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(
            AVG(amount_per_day) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
            ,2) AS average_amount,
            ROW_NUMBER() OVER (ORDER BY visited_on) AS rk
    FROM aggregate_amount
)

SELECT
    visited_on, amount, average_amount
FROM seven_day_amount
WHERE rk > 6;