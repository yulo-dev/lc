# Write your MySQL query statement below


# output grain: one row per day 
# find the MAX(amount) record per day by using DENSE_RANK, output the transaction_id
# order by transaction_id

# get the date information from day 
# DENSE_RANK() OVER (PARTITION BY day_part ORDER BY amount) -> tie will be output
# ORDER BY transaction_id

WITH date_part AS (
    SELECT
        transaction_id, day, amount,
        DATE_FORMAT(day, '%Y-%m-%d') AS day_part
    FROM Transactions
),

max_amount AS (
    SELECT 
        transaction_id, day, amount,
        DENSE_RANK() OVER (PARTITION BY day_part ORDER BY amount DESC) AS rk
    FROM date_part
)

SELECT
    transaction_id
FROM max_amount
WHERE rk = 1
ORDER BY transaction_id;