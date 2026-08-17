# Write your MySQL query statement below
select firstname,lastname,city,state
from person as P
left join address as a 
on P.personId=a.personId;

