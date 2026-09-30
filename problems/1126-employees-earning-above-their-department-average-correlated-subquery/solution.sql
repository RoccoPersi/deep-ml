-- your query
SELECT id, name, department,salary
FROM employees e
WHERE salary > (SELECT AVG(salary)
                FROM employees e2
                WHERE e.department = e2.department)
