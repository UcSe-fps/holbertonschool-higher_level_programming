-- this will be something
SELECT cities.id, cities.name, states.name
FROM cities
	JOIN states ON cities.states_id = states_id
ORDER BY cities.id ASC;
