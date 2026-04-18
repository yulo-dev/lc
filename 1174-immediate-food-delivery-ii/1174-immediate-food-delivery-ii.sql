# Write your MySQL query statement below

WITH first_date AS (
    SELECT
        customer_id, MIN(order_date) as first_order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT 
    ROUND(
        AVG(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1.0 ELSE 0 END) * 100
    ,2) as immediate_percentage

FROM Delivery AS d JOIN first_date AS f ON d.customer_id = f.customer_id and d.order_date = f.first_order_date;