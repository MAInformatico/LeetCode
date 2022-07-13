select stock_name, sum(price) as capital_gain_loss
from (select stock_name, operation operation_day,
    case when operation="buy"
    then -price when operation="sell"
    then price
        end
    as price
 from stocks) as st 
group by stock_name;
