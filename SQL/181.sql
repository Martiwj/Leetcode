

SELECT e1.name
FROM employee AS e1
WHERE e1.salary > (SELECT e2.salary FROM employee AS e2
    WHERE e2.id = e1.managerid);
    