-- A company's executives are interested in seeing who earns the most money in each of the company's departments. 
-- A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
-- Write an SQL query to find the employees who are high earners in each of the departments.

-- CTE returns department, employee, salary and distinct salary rank columns. 
WITH r AS (
SELECT 
d.name AS 'Department',
e.name AS 'Employee',
e.salary,
-- dense_rank() returns the rank of each row within a result set partition, with no gaps in the ranking values. 
-- The rank of a specific row is one plus the number of distinct rank values that come before.
DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS 'rank'
FROM employee e
LEFT OUTER JOIN department d
ON d.ID = e.departmentID)

-- returns department, employee, and salary of 'high earners' (rank top 3) 
SELECT 
r.Department,
r.Employee,
r.salary 
FROM r 
WHERE r.rank <= 3