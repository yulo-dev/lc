# Write your MySQL query statement below


# for each product, get the most recent order 
WITH ranked AS (
    SELECT
        p.product_name,
        o.product_id,
        o.order_id,
        o.order_date,
        DENSE_RANK() OVER (PARTITION BY o.product_id ORDER BY o.order_date DESC) AS rk
    FROM Products AS p
    JOIN Orders AS o
    ON p.product_id = o.product_id 
)

SELECT
    product_name, product_id, order_id, order_date
FROM ranked
WHERE rk = 1
ORDER BY product_name, product_id, order_id;