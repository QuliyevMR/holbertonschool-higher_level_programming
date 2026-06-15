-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- Uses a subquery to find California's ID without using JOIN
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
