# Write your MySQL query statement below

# >= 1 positive count then >= 1 negative count
# recovery time: first negative test after first Positive test - first positive test
# only patients with BOTH a positive & a later negative tests will be included
# order: recovery_time, patient_name

#I would break this problem into two steps.
#First, I would get each patient’s first positive test date.
#Second, I would look for the earliest negative test date that happened after that positive date.
#Then I could calculate the recovery time using the difference between those two dates.
#At the end, I would join this result with the Patients table to return the patient information.


WITH pos_and_neg AS (
    SELECT 
        p.patient_id, 
        p.test_date AS positive_date, 
        n.test_date AS negative_date, 
        ROW_NUMBER() OVER (PARTITION BY p.patient_id ORDER BY p.test_date) AS rk_positive_time,
        ROW_NUMBER() OVER (PARTITION BY n.patient_id ORDER BY n.test_date) AS rk_negative_time
    FROM covid_tests AS p
    JOIN covid_tests AS n
    ON p.patient_id = n.patient_id AND p.result = "Positive" AND n.result = "Negative" AND p.test_date < n.test_date 
),

calculate_recovery_time AS (
    SELECT 
        patient_id,
        DATEDIFF(negative_date, positive_date) AS recovery_time
    FROM pos_and_neg 
    WHERE rk_positive_time = 1 AND rk_negative_time = 1
)

SELECT
    p.patient_id, 
    p.patient_name, 
    p.age,
    c.recovery_time

FROM patients AS p 
JOIN calculate_recovery_time AS c
ON p.patient_id = c.patient_id
ORDER BY recovery_time, patient_name;

