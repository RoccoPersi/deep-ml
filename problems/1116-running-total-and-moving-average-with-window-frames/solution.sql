-- your query
SELECT s.day, s.amount,
       SUM(s.amount) OVER (ORDER BY s.day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total,
       AVG(s.amount) OVER (ORDER BY s.day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales s
ORDER BY s.day;

