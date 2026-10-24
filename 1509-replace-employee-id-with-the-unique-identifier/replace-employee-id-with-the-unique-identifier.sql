# Write your MySQL query statement below
select unique_id,name
from employees as e left join EmployeeUNI
on e.id=EmployeeUNI.id
