# Write your MySQL query statement below

#filter the people >= 100
#assign row number by id & visit_date
#caluculate visit_date - row number as grouping key
#count the number of rows per grouping key, and filter the number >= 3

# grain: one row per id per visite_date
WITH one_hundred_or_more AS (
    SELECT
        id, visit_date, people
    FROM Stadium WHERE people >= 100
),

# grain: one row per id per visite_date
ranked_row AS (
    SELECT
        id, visit_date, people,
        ROW_NUMBER() OVER (ORDER BY id) AS rk
    FROM one_hundred_or_more
),

# grain: one row per id per visite_date
# -- calculate difference between date & rk
calculate_diff AS (
    SELECT
        id, visit_date, people,
        id - rk AS group_id
    FROM ranked_row
),

# grain: one row per group_id
# -- count the number of rows per group to get the consecutive records
grouped AS (
    SELECT 
        group_id
    FROM calculate_diff 
    GROUP BY group_id
    HAVING COUNT(*) >= 3
)

#join back to get id, visit_date, people by using group_id
SELECT 
    c.id, c.visit_date, c.people
FROM calculate_diff AS c 
JOIN grouped AS g
ON c.group_id = g.group_id
ORDER BY c.visit_date;