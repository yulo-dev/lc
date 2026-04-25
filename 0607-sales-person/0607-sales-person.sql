# Write your MySQL query statement below

# join orders & company table
WITH order_red AS (
    SELECT
        c.com_id, o.sales_id
    FROM Company AS c
    JOIN Orders AS o
    ON c.com_id = o.com_id 
    WHERE c.name = 'RED'
)

# join SalesPerson & cte to get sales who does not relate to "RED"
SELECT
    s.name
FROM SalesPerson AS s
LEFT JOIN order_red AS o
ON s.sales_id = o.sales_id 
WHERE o.sales_id IS NULL;