select us.user_id as "buyer_id", us.join_date as "join_date", coalesce(count(ord.buyer_id),0) as "orders_in_2019"
from Users us
left outer join Orders ord
on us.user_id = ord.buyer_id
and ord.order_date LIKE '2019%'
group by us.user_id;
