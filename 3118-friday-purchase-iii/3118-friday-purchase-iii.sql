# Write your MySQL query statement below


#DAYOFWEEK -> SUN - SAT -> 1 ~ 7
#WEEKDAY -> MON - SUN -> 0 ~ 6

#select date between '2023-11-01' and '2023-11-31' & select DAYOFWEEK(date) = 6 & CEIL(DAY(date) / 7)
#join with user table to get the membership 
#SUM(amount_spend) OVER (PARTITION BY week of month)
#order by week, memebership


# -- (0) create frame
WITH weeks AS (
    SELECT
        1 AS week_of_month
    UNION ALL
    SELECT 
        2
    UNION ALL
    SELECT
        3
    UNION ALL
    SELECT
        4
),

membership AS (
    SELECT
        'Premium' AS membership
    UNION ALL
    SELECT
        'VIP'
),

skeleton AS (
    SELECT
        w.week_of_month,
        m.membership
    FROM weeks AS w
    CROSS JOIN membership AS m
),
    
# -- (1) select valid window
valid_window AS (
    SELECT 
         user_id, purchase_date, amount_spend,
         CEIL(DAY(purchase_date) / 7) AS week_of_month
    FROM Purchases
    WHERE (purchase_date BETWEEN '2023-11-01' AND '2023-11-30') AND (DAYOFWEEK(purchase_date) = 6) 
),

# -- (2) get memebership
with_membership AS (
    SELECT 
        u.membership,
        v.user_id, v.purchase_date, v.amount_spend, v.week_of_month
    FROM Users AS u
    JOIN valid_window AS v
    ON u.user_id = v.user_id
)

# -- (3) sum the total amount per week_of_month and memebership
SELECT
    s.week_of_month, s.membership, 
    COALESCE(
        SUM(m.amount_spend)
    , 0) AS total_amount
FROM skeleton AS s
LEFT JOIN with_membership AS m
ON s.week_of_month = m.week_of_month AND s.membership = m.membership
GROUP BY s.week_of_month, s.membership
ORDER BY s.week_of_month, s.membership;