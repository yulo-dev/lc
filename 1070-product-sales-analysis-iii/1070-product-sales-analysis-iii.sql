# Write your MySQL query statement below

WITH first_year_records AS (
    SELECT
        product_id, 
        year,
        DENSE_RANK() OVER (PARTITION BY product_id ORDER BY year) AS rk, 
        quantity, 
        price
    FROM Sales
)

SELECT
    product_id, year AS first_year, quantity, price
FROM first_year_records
WHERE rk = 1;