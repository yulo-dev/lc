# Write your MySQL query statement below


# TOP 5% per state
# order: state, fraud_score desc, policy_id

# PERCENT_RANK() OVER (PARTITION BY state ORDER BY fraud_score DESC) AS pct_rank
# filter pct_rank <= 0.05

WITH pct_rank AS (
    SELECT
        policy_id, state, fraud_score,
        PERCENT_RANK() OVER (PARTITION BY state ORDER BY fraud_score DESC) AS pct_rank
    FROM Fraud
)

SELECT  
    policy_id, state, fraud_score
FROM pct_rank
WHERE pct_rank <= 0.05
ORDER BY state, fraud_score DESC, policy_id;