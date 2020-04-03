select ifnull( (select distinct Salary from Employee ORDER BY Salary DESC LIMIT 1,1), null ) as SecondHighestSalary;
