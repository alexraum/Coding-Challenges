-- Version 1
select sq1.month, sq1.total_count, sq1.total_amount, sq2.mike_count, sq2.mike_amount, sq3.jon_count, sq3.jon_amount
from (select extract(month from payment_date) as month, count(*) as total_count, sum(amount) as total_amount
     from payment
     group by month) as sq1
inner join (select extract(month from payment_date) as month, count(*) as mike_count, sum(amount) as mike_amount
            from payment
            where staff_id = 1
            group by month) as sq2
on sq1.month = sq2.month
inner join (select extract(month from payment_date) as month, count(*) as jon_count, sum(amount) as jon_amount
            from payment
            where staff_id = 2
            group by month) as sq3
on sq2.month = sq3.month;


-- Version 2

-- use ctes to define and assign names to queries

with q1 as ( -- overall number and total amount of payments, across months
    select extract(month from payment_date) as month, count(*) as total_count, sum(amount) as total_amount
    from payment
    group by month
), q2 as ( -- number and total amount of payments in Mike's store, across months
    select extract(month from payment_date) as month, count(*) as mike_count, sum(amount) as mike_amount
    from payment
    where staff_id = 1
    group by month
), q3 as ( -- number and total amount of payments in Jon's store, across months
    select extract(month from payment_date) as month, count(*) as jon_count, sum(amount) as jon_amount
    from payment
    where staff_id = 2
    group by month
)

-- join queries on month and select fields of interest
select q1.month, q1.total_count, q1.total_amount, q2.mike_count, q2.mike_amount, q3.jon_count, q3.jon_amount
from q1
inner join q2
on q1.month = q2.month
inner join q3
on q2.month = q3.month
order by month;
