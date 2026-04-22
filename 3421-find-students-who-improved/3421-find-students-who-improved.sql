# Write your MySQL query statement below


# for each student, count the number taken for each subject, filter count >= 2
# then, get the first and last score for these subject and student 
# then, if last score > first score: output
# sort: student_id, subject 


WITH subject_taken_times AS (
    SELECT 
       student_id,  subject, COUNT(*) AS taken_times
    FROM Scores 
    GROUP BY student_id, subject
    HAVING COUNT(*) >= 2
),

rank_exam_date AS (
    SELECT 
        s.student_id, s.subject, exam_date, score,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_rk,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS last_rk
    FROM Scores AS s 
    JOIN subject_taken_times AS s2
    ON s.student_id = s2.student_id AND s.subject = s2.subject
)

SELECT
    r1.student_id, r1.subject, 
    r1.score AS first_score, r2.score AS latest_score 
FROM rank_exam_date AS r1
JOIN rank_exam_date AS r2
ON r1.student_id = r2.student_id AND r1.subject = r2.subject AND r1.exam_date < r2.exam_date AND r1.first_rk = 1 AND r2.last_rk = 1
HAVING r1.score < r2.score 
ORDER BY student_id, subject
;