-- Script to display the average temperature (Fahrenheit) 
-- By city ordered by temperature (descending).

SELECT city, ROUND(AVG(temp)) AS avg_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
