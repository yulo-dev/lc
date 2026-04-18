# Write your MySQL query statement below

SELECT 
    DATE_FORMAT(trans_date, "%Y-%m") AS month,
    country, 
    COUNT(*) as trans_count, SUM(CASE WHEN state = "approved" THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END) AS approved_total_amount

FROM Transactions
GROUP BY country, EXTRACT(YEAR FROM trans_date), EXTRACT(MONTH FROM trans_date);


# %Y: 四位數年份     -> 2022
# %y: 兩位數年份    -> 22
# %m: 兩位數月份（01-12）-> 04
# %M: 月份英文全名  -> April
# %d: 兩位數日期（01-31）-> 16
# %D: 日期加序數    -> 16th
# %H: 24小時制小時 -> 14
# %h: 12小時制小時 -> 02