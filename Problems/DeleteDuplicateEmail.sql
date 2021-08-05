delete d from Person as p, Person as d where p.Email = d.Email and p.Id < d.Id;
