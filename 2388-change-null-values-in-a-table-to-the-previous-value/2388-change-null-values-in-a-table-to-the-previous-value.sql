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


# OK so I need to fill NULLs with the most recent non-NULL value above them.
# The trick is that COUNT ignores NULLs. So if I do a running COUNT of the drink column, 
# every NULL row gets the same count as the previous non-NULL row. 
# That gives me a group identifier. Then within each group, I just take the MAX to grab the one non-NULL value and apply it to the whole group.


# First I need to preserve the original row order, so let me add a ROW_NUMBER. 
# then I'll do a running COUNT of drink ordered by that row number. 
# NULLs won't increment the count, so they stay in the same group as the previous non-NULL.
# now I just PARTITION BY that group and #take MAX of drink.


# This is essentially a forward-fill problem. 
# The key insight is that COUNT skips NULLs, so a running COUNT creates natural groups between non-NULL values.