# Write your MySQL query statement below

SELECT query_name, 
    ROUND(
        COALESCE(
            AVG(rating * 1.0 / NULLIF(position,0))
        ,0)
    ,2) AS quality, 
    ROUND(
        COALESCE(
            AVG(CASE WHEN rating < 3 THEN 1.0 ELSE 0 END) * 100
        ,0)
    ,2) AS poor_query_percentage

FROM Queries
GROUP BY query_name;