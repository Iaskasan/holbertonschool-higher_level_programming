-- list all the cities of the state of California in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id IN (
    SELECT id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
