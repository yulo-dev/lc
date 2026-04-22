# Write your MySQL query statement below

# total per user
# filter >= 5 items
# 60% reaction are the same type, per user 
# order: reaction_ratio DESC, user_id

#(1) count number of content_id per user and select number >= 5 
#(2) count the percentage of each reaction per user
#(3) if percantage >= 60%, output ration + that reaction

WITH five_contents AS (
    SELECT 
        user_id, COUNT(DISTINCT content_id) AS nums_of_content
    FROM reactions 
    GROUP BY user_id
),

percantage_of_reaction AS (
    SELECT
        r.user_id, 
        r.reaction,
        ROUND(
            COUNT(*) / f.nums_of_content
        ,2) AS ratio
    FROM reactions AS r 
    LEFT JOIN five_contents AS f
    ON r.user_id = f.user_id AND f.nums_of_content >= 5 
    GROUP BY r.user_id, r.reaction
)

SELECT
    user_id, 
    reaction AS dominant_reaction,
    ratio AS reaction_ratio

FROM percantage_of_reaction 
WHERE ratio > 0.6
ORDER BY reaction_ratio DESC, user_id;