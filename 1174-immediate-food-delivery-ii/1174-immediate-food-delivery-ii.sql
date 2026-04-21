# Write your MySQL query statement below

# immediate: same day -> percentage
# scheduled: different day
# first order: earliest date per customer (no tie)

# row number: get the first record per customer (ORDER BY order_date)
# numerator:  count of customers whose first order is immediate
# denominator: total number of customers
# percentage: numerator / denominator * 100

WITH first_orders_ranked AS (
    SELECT
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn,
        customer_id,
        order_date, customer_pref_delivery_date
    FROM Delivery
)

SELECT
    ROUND(
        AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100
        ,2) AS immediate_percentage
FROM first_orders_ranked
WHERE rn = 1;