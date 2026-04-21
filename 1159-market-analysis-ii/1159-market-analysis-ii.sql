# Write your MySQL query statement below


# for each seller, rank orders by order_date
# filter rk = 2 to keep the second order
# join Items to get the brand of that second item
# left join Users because some sellers may not have a second order
# output yes if favorite_brand = second item brand, else no

WITH rank_order AS (
    # -- rank the Orders table by order_date per seller
    # -- get the item_brand by joining Items table
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date) AS rk,
        o.item_id,
        o.seller_id,
        i.item_brand
    FROM Orders AS o JOIN Items AS i ON o.item_id = i.item_id
)

SELECT
    u.user_id AS seller_id,
    CASE 
        WHEN r.item_brand IS NOT NULL THEN 'yes' 
        ELSE 'no' 
        END AS 2nd_item_fav_brand

FROM Users AS u 
    LEFT JOIN rank_order AS r                   # -- join by favorite_brand = item_brand and rk = 2 per seller to check if the second item they sell is their fav brand
    ON u.user_id = r.seller_id AND u.favorite_brand = r.item_brand AND r.rk = 2;