# Write your MySQL query statement below


# group the missing drink and their previous non-missing drink record together 
# by using count 
# if non-missing: 1, else 0 -> increment by 1 and natually formed a order 
# after grouping, get the non-missing drink join with missing records on group id


WITH ordered AS (
    SELECT 
        *, 
        #保持原來的順序
        ROW_NUMBER() OVER () AS rn
    FROM CoffeeShop
),

grouped AS (
    SELECT *,
        # NULL 跟前面的非 NULL 分同一組
        COUNT(drink) OVER (ORDER BY rn) AS grp
    FROM ordered
)

SELECT 
    id,
    # 每組拿那個非 NULL 的值
    MAX(drink) OVER (PARTITION BY grp) AS drink
FROM grouped
order by rn;