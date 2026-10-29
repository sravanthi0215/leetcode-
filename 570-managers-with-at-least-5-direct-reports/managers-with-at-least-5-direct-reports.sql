# Write your MySQL query statement below
select e.name
from employee as e 
where e.id in 
    (select m.managerId
    from employee as m
    where m.managerId is not null
    group by m.managerid
    having count(m.managerid)>=5 )
