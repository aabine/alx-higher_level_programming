-- Select the city and maximum temperature for each city
-- during the months of July and August

SELECT city, MAX(temp) AS max_temperature
FROM temperatures
WHERE MONTH(month_data) IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
