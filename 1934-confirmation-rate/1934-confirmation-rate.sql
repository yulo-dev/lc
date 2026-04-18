# Write your MySQL query statement below
SELECT s.user_id, 
       ROUND(
        COALESCE(
            SUM(CASE WHEN c.action = "confirmed" THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(c.action),0)
            ,0)
        ,2) AS confirmation_rate

FROM Signups AS s LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY s.user_id;

#familiar with NULLIF
#-- 算任何 rate / ratio / percentage，都用這個模板
#ROUND(
#    COALESCE(
#        分子 * 1.0 / NULLIF(分母, 0)
#    , 0)
#, 2)