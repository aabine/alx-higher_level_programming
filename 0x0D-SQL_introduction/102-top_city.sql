-- Select the city and maximum temperature for each city
-- during the months of July and August

SELECT city, MAX(value) AS max_temp
FROM temperatures
WHERE MONTH(month_data) IN (7, 8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
