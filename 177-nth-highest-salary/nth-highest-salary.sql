CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary 
      from employee e
      where (select count(distinct salary)
      from employee
      where salary>e.salary)=N-1

  );
END