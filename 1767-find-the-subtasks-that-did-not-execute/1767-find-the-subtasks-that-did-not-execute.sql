# Write your MySQL query statement below
WITH RECURSIVE nums AS (
    SELECT 1 AS subtask_id #起點 (先跑 base case)
    UNION ALL
    SELECT subtask_id + 1 #往下長 (再跑 recursive part)
    FROM nums
    WHERE subtask_id < 20
),
all_subtasks AS (
    SELECT
        t.task_id,
        n.subtask_id
    FROM Tasks AS t
    JOIN nums AS n
      ON n.subtask_id <= t.subtasks_count
)
SELECT
    a.task_id,
    a.subtask_id
FROM all_subtasks AS a
LEFT JOIN Executed AS e
  ON a.task_id = e.task_id
 AND a.subtask_id = e.subtask_id
WHERE e.task_id IS NULL
ORDER BY a.task_id, a.subtask_id;