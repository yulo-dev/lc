# Write your MySQL query statement below


# 2019-01-01 to 2019-12-31
# FILTER out dates within 2019-01-01 to 2019-12-31 for Failed & Succeeded tables
# union all the two tables & flagged the date is failed or succeeded, then order by date 
# group the consecutive days together
# row_number() over (partition by flagged order by day)
# date - row_number as group key
# group them together and the min: start date, max: end date


WITH union_records AS (
    SELECT
        0 AS succeed, fail_date AS event_date
    FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'

    UNION ALL

    SELECT
        1 AS succeed, success_date AS event_date
    FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),

# use the date - ROW_NUMBER trick to create grouping key, group the consecutive days together
# "2026-01-01" row_numer = 1 -> 2025-12-31
# "2026-01-02" row_numer = 2 -> 2025-12-31
# "2026-01-03" row_numer = 3 -> 2025-12-31
# "2026-01-05" row_numer = 4 -> 2026-01-01

ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY succeed ORDER BY event_date) AS rk
    FROM union_records
),

grouped AS (
    SELECT
        *,
        DATE_SUB(event_date, INTERVAL rk DAY) AS grp
    FROM ranked
)

SELECT
    CASE WHEN succeed = 1 THEN 'succeeded'
         ELSE 'failed' END AS period_state,
    MIN(event_date) AS start_date,
    MAX(event_date) AS end_date
FROM grouped
GROUP BY period_state, grp
ORDER BY start_date;
