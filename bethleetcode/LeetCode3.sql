-- The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.
-- Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". 
-- Round Cancellation Rate to two decimal points.
SELECT 
t.request_at Day, 
round(sum(CASE 
	WHEN t.status = 'completed' 
    THEN 0 
    ELSE 1 
    END) / count(*), 2) 'Cancellation Rate'
FROM trips t
INNER JOIN users u 
ON t.client_Id = u.users_Id AND u.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at