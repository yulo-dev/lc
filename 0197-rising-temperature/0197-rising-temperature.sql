# Write your MySQL query statement below
select b.Id
from weather as a inner join weather as b on datediff(b.recordDate, a.recordDate) = 1
where a.temperature < b.temperature 