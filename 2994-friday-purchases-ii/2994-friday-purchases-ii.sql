# Write your MySQL query statement below

# SELECT purchase_date BETWEEN '2023-11-01' AND '2023-11-30' & DAYOFWEEK(purchase_date) = 6
# WEEK OF MONTH: CEIL(DAY(purchase_date) / 7)  
# SUM(amount_spend) OVER (PARTITION BY WEEK OF MONTH) 



# -- (1) create the timeframe for each friday BETWEEN '2023-11-01' AND '2023-11-30'
WITH RECURSIVE dates AS (
    SELECT 
        DATE('2023-11-01') AS purchase_date

    UNION ALL

    SELECT
        DATE_ADD(purchase_date, INTERVAL 1 DAY) 
    FROM dates
    WHERE purchase_date < '2023-11-30'
),

frame AS (
    SELECT
        CEIL(DAY(purchase_date) / 7) AS week_of_month,
        purchase_date
    FROM dates
    WHERE DAYOFWEEK(purchase_date) = 6
),

# -- (2) select the valid window from Purchases
valid_window AS (
    SELECT 
        purchase_date, amount_spend,
        CEIL(DAY(purchase_date) / 7) AS week_of_month
    FROM Purchases
    WHERE purchase_date BETWEEN '2023-11-01' AND '2023-11-30' AND DAYOFWEEK(purchase_date) = 6
)

# -- (3) join the two table & sum the amount per week 
SELECT
    f.week_of_month, 
    f.purchase_date,
    COALESCE(
        SUM(v.amount_spend)
    ,0) AS total_amount

FROM frame AS f
LEFT JOIN valid_window AS v
ON f.week_of_month = v.week_of_month
GROUP BY f.week_of_month, f.purchase_date
ORDER BY f.week_of_month;


