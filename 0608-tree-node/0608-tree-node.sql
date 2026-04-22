# Write your MySQL query statement below

#Root: p_id is null
#Inner: in p_id and p_id is not null
#else: Leaf

SELECT
    id,
    CASE WHEN p_id IS NULL THEN "Root"
         WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN "Inner"
         ELSE "Leaf"
         END AS type

FROM Tree;