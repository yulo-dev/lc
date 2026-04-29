# Write your MySQL query statement below


# CONVERSION RATE: (100 * total number of purchases for the member) / total number of visits for the member.
# numerator: count(*) from Purchases group by member_id
# denominator: count(*) from Visits group by member_id

# -- (1) calculate pruchase_time per visit
WITH visit_and_purchase AS (
    SELECT
        v.visit_id, v.member_id, v.visit_date,
        CASE WHEN p.visit_id IS NOT NULL THEN 1 ELSE 0 END AS purchase
    FROM Visits AS v
    LEFT JOIN Purchases AS p
    ON v.visit_id = p.visit_id
),

# -- (2) calculate Purchases & visits for the member
# -- (3) calculate conversion rate per member
visit_time AS (
    SELECT
        member_id,
        SUM(purchase) AS purchase_time,
        COUNT(*) AS visit_time,
        COALESCE(
            SUM(purchase) * 100 / NULLIF(COUNT(*),0)
        ,0) AS rate
    FROM visit_and_purchase
    GROUP BY member_id
)

SELECT
    m.member_id, m.name,
    CASE WHEN v.rate >= 80 THEN 'Diamond'
         WHEN v.rate >= 50 THEN 'Gold'
         WHEN v.rate >= 0 AND visit_time > 0 THEN 'Silver'
         ELSE 'Bronze'
         END AS category
FROM Members AS m
LEFT JOIN visit_time AS v
ON m.member_id = v.member_id
;
