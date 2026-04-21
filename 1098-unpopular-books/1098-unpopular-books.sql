# Write your MySQL query statement below


# for each book id, get the aggregate sum between '2018-06-23' AND '2019-06-23'
# join with Books on book_id, where the available date is before/on '2019-05-23' 
# and the aggregate sum is less than 10 in the last year


WITH aggregate_quantity_last_year AS (
    SELECT
        # -- get the aggregate sum between '2018-06-23' AND '2019-06-23' for each book id
        book_id, 
        SUM(quantity) AS quantity_per_book
    FROM Orders
    WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
    GROUP BY book_id
)

# -- join with books to filter the available date is before/on 2019-05-23
SELECT
    b.book_id, b.name
FROM Books AS b 
LEFT JOIN aggregate_quantity_last_year AS a
    ON b.book_id = a.book_id
WHERE b.available_from <= '2019-06-23' - INTERVAL 1 MONTH 
    AND COALESCE(a.quantity_per_book, 0) < 10; #不加coalesce的話 空值<10 不算true