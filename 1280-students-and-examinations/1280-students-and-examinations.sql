# Write your MySQL query statement below
SELECT a.student_id, a.student_name, b.subject_name, COUNT(c.subject_name) as attended_exams
FROM Students AS a 
CROSS JOIN Subjects AS b
LEFT JOIN Examinations AS c ON a.student_id = c.student_id and b.subject_name = c.subject_name
GROUP BY a.student_id, a.student_name, b.subject_name
ORDER BY a.student_id;

#練習CROSS JOIN