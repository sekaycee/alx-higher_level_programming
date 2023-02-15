-- List all the cities of California that can be found in database 'hbtn_0d_usa'
SELECT id, name
  FROM cities
 WHERE state_id = -- Get state_id via a subquery
       (SELECT id
          FROM states
         WHERE name = 'California')
 ORDER BY id;
