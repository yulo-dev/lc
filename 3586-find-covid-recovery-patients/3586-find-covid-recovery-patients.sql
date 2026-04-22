# Write your MySQL query statement below




WITH first_positive AS (
    SELECT 
        patient_id, 
        MIN(test_date) AS first_positive_date
    FROM covid_tests 
    WHERE result = "Positive"
    GROUP BY patient_id
),

first_negative_after_positive AS (
    SELECT 
        fn.patient_id,
        MIN(fn.test_date) AS first_negative_date
    FROM covid_tests AS fn  
    JOIN first_positive AS fp  
      ON fn.patient_id = fp.patient_id
     AND fn.test_date > fp.first_positive_date
    WHERE fn.result = "Negative"
    GROUP BY patient_id
)

SELECT
    p.patient_id, 
    p.patient_name, 
    p.age,
    DATEDIFF(fn.first_negative_date, fp.first_positive_date) AS recovery_time

FROM patients AS p 
JOIN first_positive AS fp
  ON p.patient_id = fp.patient_id
JOIN first_negative_after_positive AS fn
  ON p.patient_id = fn.patient_id
ORDER BY recovery_time, patient_name;