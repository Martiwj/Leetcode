SELECT eu.unique_id AS unique_id, e.name AS name
FROM Employees e 
lEFT JOIN EmployeeUNI eu ON e.id = eu.id;