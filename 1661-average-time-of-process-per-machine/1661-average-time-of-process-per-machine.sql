# Write your MySQL query statement below

SELECT a.machine_id, round(avg(b.timestamp - a.timestamp),3) AS processing_time
FROM Activity as a left join Activity as b
ON a.machine_id = b.machine_id and a.process_id = b.process_id
WHERE a.activity_type = "start" and b.activity_type = "end"
group by a.machine_id;

#要注意avg那邊 他的分母就是根據：這個 machine_id 這一組裡，有幾筆被拿來算平均的資料
#也就是a.timestamp跟b.timestamp都非空
#因為只要其中一個是 NULL：
#3.5 - NULL = NULL
#NULL - 1.2 = NULL
#結果就還是 NULL，那這筆就不會被 AVG(...) 算進去。