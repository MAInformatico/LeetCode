SELECT weather.id AS 'Id'
FROM weather
JOIN weather wea ON DATEDIFF(weather.recordDate, wea.recordDate) = 1 AND weather.Temperature > wea.Temperature;
