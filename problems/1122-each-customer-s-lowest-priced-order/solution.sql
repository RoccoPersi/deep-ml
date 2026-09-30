-- your query
SELECT order_id, customer_id, amount
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount) AS rn
    FROM orders
) t
WHERE rn = 1
ORDER BY customer_id;