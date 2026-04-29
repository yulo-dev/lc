# Write your MySQL query statement below

# most recent 3 order per user
# order: customer_name, customer_id, order_date desc


WITH ranked AS (
    SELECT
        o.customer_id, o.order_id, o.order_date,
        c.name AS customer_name,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.order_date DESC) AS rk
    FROM Orders AS o
    JOIN Customers AS c
    ON o.customer_id = c.customer_id
)

SELECT 
    customer_name, customer_id, order_id, order_date
FROM ranked
WHERE rk <= 3
ORDER BY customer_name, customer_id, order_date DESC;