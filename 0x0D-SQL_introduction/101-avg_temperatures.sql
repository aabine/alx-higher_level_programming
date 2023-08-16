-- Script to display the average temperature (Fahrenheit) 
-- By city ordered by temperature (descending).

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
