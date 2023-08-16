-- This query retrieves the maximum temperature
-- for each state from the 'temperatures' table

SELECT state, MAX(value) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
