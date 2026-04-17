# Write your MySQL query statement below

SELECT a.id
FROM Weather AS a JOIN Weather AS b ON DATEDIFF(a.recordDate, b.recordDate) = 1
where a.temperature > b.temperature;

#DATEDIFF(a.recordDate, b.recordDate) = 1 這代表a是今天 b是昨天
#所以where的地方也是 a.temperature > b.temperature 代表 今天溫度 > 昨天溫度
#所以select的地方要選a.id 也就是今天的