# Write your MySQL query statement below

#3-day rolling average per user (to 2 decimal points)
#might have skip dates: can not count the average of n consecutive days
#get the 3-day consecutive window
#based on that cte to calculate average by using window function: AVG() OVER (ORDER BY ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)


WITH ranked AS (
    SELECT 
        user_id, steps_count, steps_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY steps_date) AS rk
    FROM Steps
),

grouped AS (
    SELECT 
        user_id, steps_count, steps_date,
        DATE_SUB(steps_date, INTERVAL rk DAY) AS grp
    FROM ranked
),

valid_rows AS (
    SELECT 
        user_id, steps_count, steps_date, grp
    FROM grouped
    WHERE (user_id, grp) IN (
        SELECT 
            user_id, grp
        FROM grouped
        GROUP BY user_id, grp
        HAVING COUNT(*) >= 3 #先找出哪些 (user_id, grp) 合格 (這邊grain是one row per user per grp), 再用這兩個key去抓所有吻合的records
    )                        #where是把所有屬於這些合格 key 的原始 rows 全部保留下來，所以會從「一組一列」回到「一組多列」。
),

#需要刪調前面還沒滿足到三筆的records
calculate_avg AS (
    SELECT
        user_id, steps_date,
        ROUND(
            AVG(steps_count) OVER (
                PARTITION BY user_id, grp 
                ORDER BY steps_date 
                ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
            ,2) AS rolling_average,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, grp
            ORDER BY  steps_date
        ) AS rn
    FROM valid_rows
)

SELECT
    user_id, steps_date, rolling_average
FROM calculate_avg
WHERE rn >= 3
ORDER BY user_id, steps_date;