# Write your MySQL query statement below

# -- remove duplicate records
WITH unique_login AS (
    SELECT DISTINCT
        id, login_date
    FROM Logins
),
# -- rank each row by id & login date
ranked_login AS (
    SELECT
        id, login_date,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date) AS rk
    FROM unique_login
),
grouped AS (
    SELECT
        id, login_date,
        DATE_SUB(login_date, INTERVAL rk DAY) AS grp
    FROM ranked_login
),
active_users AS (
    SELECT DISTINCT
        id
    FROM grouped
    GROUP BY id, grp
    HAVING COUNT(*) >= 5
)
SELECT
    a1.id, a1.name
FROM Accounts AS a1
JOIN active_users AS a2
  ON a1.id = a2.id
ORDER BY a1.id
;