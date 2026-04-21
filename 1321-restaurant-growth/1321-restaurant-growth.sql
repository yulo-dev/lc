# Write your MySQL query statement below


# no date gaps between rows
# may have same date appear more than one row


WITH total_amout_per_day AS (
    SELECT 
        visited_on, SUM(amount) AS total_amout
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
),

total_amout_in_window AS (
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

    FROM total_amout_per_day
    GROUP BY visited_on
)

SELECT 
    visited_on, amount, average_amount
FROM total_amout_in_window
WHERE RN >=7;