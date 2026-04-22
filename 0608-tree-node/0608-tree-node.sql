# Write your MySQL query statement below

#Root: p_id is null
#Inner: in p_id and p_id is not null
#else: Leaf

WITH unique_pid AS (
    SELECT DISTINCT p_id
    FROM Tree WHERE p_id IS NOT NULL
)
SELECT
    t.id,
    CASE WHEN t.p_id IS NULL THEN "Root"
         WHEN t2.p_id IS NULL THEN "Leaf"
         ELSE "Inner"
         END AS type

FROM Tree AS t LEFT JOIN unique_pid AS t2
ON t.id = t2.p_id;