# Write your MySQL query statement below

# aggregate the score_points per day for each gender

SELECT
    gender, 
    day,
    SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY gender, day;