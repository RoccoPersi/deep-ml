-- your query
SELECT min(id) as id, email
from person
group by iemail
order by id 
