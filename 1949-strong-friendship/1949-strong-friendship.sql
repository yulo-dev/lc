# Write your MySQL query statement below

#雙向化友誼
WITH TwoWayFriendship AS (
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM Friendship
)
SELECT
    a.user_id AS user1_id,
    b.user_id AS user2_id,
    COUNT(*) AS common_friend
FROM TwoWayFriendship AS a
JOIN TwoWayFriendship AS b
  #找兩個不同的人，剛好有同一個朋友
  ON a.friend_id = b.friend_id AND a.user_id < b.user_id

#再確認這兩個人本來就是朋友
WHERE EXISTS (
    SELECT 1
    FROM Friendship AS f
    WHERE f.user1_id = a.user_id AND f.user2_id = b.user_id
)

#在算 每一對朋友，共有幾個共同朋友
GROUP BY a.user_id, b.user_id
HAVING COUNT(*) >= 3;