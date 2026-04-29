# Write your MySQL query statement below


# output grain: one row per account_id per day, ORDER BY account_id, day
# rolling sum of amoun per account_id

# if the type = Deposit: amount, if the type = Withdraw, amount * -1
# rolling sum: SUM(amount) OVER (PARTITION BY account_id ORDER BY day)

WITH type_of_amount AS (
    SELECT
        account_id, day, type,
        # update the value of amount for later rolling sum use
        CASE WHEN type = 'Withdraw' THEN amount * -1
        ELSE amount END AS amount
    FROM Transactions
)

SELECT
    account_id, day,
    COALESCE( 
        SUM(amount) OVER (PARTITION BY account_id ORDER BY day)
        ,0) AS balance
FROM type_of_amount
ORDER BY account_id, day;