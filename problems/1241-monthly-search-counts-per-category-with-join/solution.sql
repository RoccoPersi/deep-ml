-- your query
SELECT c.category_name, EXTRACT(MONTH FROM s.searched_at) AS month, COUNT(*)
FROM categories c 
JOIN searches s ON c.category_id = s.category_id
WHERE EXTRACT(YEAR FROM s.searched_at) = 2023
GROUP BY  c.category_name, EXTRACT(MONTH FROM s.searched_at)
