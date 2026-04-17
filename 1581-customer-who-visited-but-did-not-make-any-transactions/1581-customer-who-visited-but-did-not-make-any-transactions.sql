# Write your MySQL query statement below
SELECT a.customer_id, COUNT(*) as count_no_trans
FROM Visits AS a LEFT JOIN Transactions AS b ON a.visit_id = b.visit_id
WHERE b.transaction_id IS NULL
group by a.customer_id;

#這題有點小故意 他就是要讓他一對多然後膨脹 最後把不在b的資料保留下來 去用customer_id當作一組 計算次數
#一開始有點卡住 沒注意到是用去用customer_id當作一組 所以一直在想怎麼解決膨脹跟計算次數
