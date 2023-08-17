-- This query selects the id and name of cities in the state of California
-- The cities table is joined with the states table based on the state_id column
-- The result is ordered by the city id in ascending order

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
