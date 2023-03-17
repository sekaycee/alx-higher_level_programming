#!/usr/bin/python3
''' List all cities from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC')
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    conn.close()
