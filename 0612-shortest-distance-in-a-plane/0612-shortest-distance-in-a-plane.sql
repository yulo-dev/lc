# Write your MySQL query statement below

#SQRT開根號
#POW(a, b) -> 意思：a 的 b 次方

SELECT 
    ROUND(
        MIN(
            SQRT(
                POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)
                )
        )
    ,2) AS shortest

FROM Point2D AS p1 
JOIN Point2D AS p2 ON p1.x != p2.x OR p1.y != p2.y;