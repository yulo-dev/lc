# Write your MySQL query statement below

# dedup the records because the description mentioned This table may contain duplicates rows
# use ROW_NUMBER to rank by startdate DESC partition by username
# use COUNT to check whether this username has only one record or not
# filter rk = 2 or count = 1

# dedup
WITH deduped AS (
    SELECT 
        DISTINCT username, activity, startDate, endDate
    FROM UserActivity
),

# ranked
ranked AS (
    SELECT
        username, activity, startDate, endDate,
        ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) AS rk,
        COUNT(*) OVER (PARTITION BY username) AS cnt #to check if the username has only one record 
    FROM deduped
)

SELECT
    username, activity, startDate, endDate
FROM ranked
WHERE (rk = 2) or (cnt = 1);