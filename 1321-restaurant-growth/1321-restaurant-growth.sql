# Write your MySQL query statement below


# no date gaps between rows
# may have same date appear more than one row


WITH daily_sales AS (
    SELECT 
        visited_on, SUM(amount) AS total_amout
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
),

rolling_7day AS (
    SELECT 
        visited_on, 
        SUM(total_amout) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS amount,

        ROUND(
            AVG(total_amout) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            )
            ,2) AS average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn

    FROM daily_sales
    GROUP BY visited_on
)

SELECT 
    visited_on, amount, average_amount
FROM rolling_7day
WHERE rn >=7;