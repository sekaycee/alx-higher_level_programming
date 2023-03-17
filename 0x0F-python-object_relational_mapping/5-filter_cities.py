#!/usr/bin/bash
''' List cities by state from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost',
                           port=3600,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT cities.name FROM cities LEFT JOIN states \
        ON states.id = cities.state_id WHERE states.name LIKE BINARY (%s) \
        ORDER BY cities.id ASC', (sys.argv[4],))
    cities = cur.fetchall()
    print(', '.join([city for city in cities]))

    cur.close()
    conn.close()
