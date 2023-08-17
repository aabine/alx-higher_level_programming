-- Select the id, name of cities, and name of states from the cities table
-- Join the cities table with the states table on the state_id column
-- Order the results by cities.id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
