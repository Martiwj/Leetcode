
SELECT a.city, a.state, p.firstname, p.lastname
FROM address AS a
RIGHT JOIN person AS p USING(personid);