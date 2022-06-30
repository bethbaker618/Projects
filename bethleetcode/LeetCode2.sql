-- Write an SQL query to find all numbers that appear at least three times consecutively.
-- Self join logs table to find 3 consecutive numbers on id, id + 1, and id + 2 and numbers are all equal. 

SELECT 
DISTINCT first.num AS ConsecutiveNums 
FROM logs first 
INNER JOIN Logs second
ON first.id = second.id + 1 AND first.num = second.num
INNER JOIN logs third
ON third.id = second.id + 2 AND first.num = third.num 