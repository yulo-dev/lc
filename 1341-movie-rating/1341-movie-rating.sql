# Write your MySQL query statement below

(
SELECT u.name AS results
FROM MovieRating AS m 
JOIN Users AS u ON m.user_id = u.user_id
GROUP BY m.user_id
ORDER BY COUNT(m.user_id) DESC, u.name
LIMIT 1
)

UNION ALL
#要用UNION ALL 因為名字可能剛好一樣

(
SELECT m2.title AS results
FROM MovieRating AS m 
JOIN Movies AS m2 ON m.movie_id = m2.movie_id
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m.movie_id
ORDER BY AVG(m.rating) DESC, m2.title 
LIMIT 1
)
;