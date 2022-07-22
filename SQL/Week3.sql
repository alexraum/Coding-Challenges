-- SQL Exercise: Week 3

select name as product_name, extract(year from date) as year, extract(month from date) as month, extract(day from date) as day, sum(price*count) as total
from products as p, sales as s, sales_details as sd -- select tables with aliases
where p.id = sd.product_id and s.id = sd.sale_id -- inner join on appropriate columns
group by 1, rollup(2, 3, 4) -- group by and rollup to find total sales by day, month, and year (for each product)
order by 1, 2, 3, 4; -- order the results
