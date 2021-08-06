# Write your MySQL query statement below
select todayWeather.Id
from Weather todayWeather
join Weather yesterdayWeather on todayWeather.temperature > yesterdayWeather.temperature and subdate(todayWeather.recordDate, 1) = yesterdayWeather.recordDate;
