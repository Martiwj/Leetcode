-- Write your PostgreSQL query statement below
-- Game Play Analysis I

SELECT player_id,  MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id; 