#!/usr/bin/python3
''' List cities by state from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT cities.name FROM cities WHERE cities.state_id = \
                 (SELECT states.id FROM states WHERE states.name = (%s)) \
                 GROUP BY cities ORDER BY cities.id ASC', (sys.argv[4],))

    cities = cur.fetchall()
    print(', '.join([city for city in cities]))

    cur.close()
    conn.close()
