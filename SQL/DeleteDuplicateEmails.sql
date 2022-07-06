DELETE aux1
FROM Person aux1 JOIN Person aux2 ON aux1.email = aux2.email
WHERE aux1.id > aux2.id;
