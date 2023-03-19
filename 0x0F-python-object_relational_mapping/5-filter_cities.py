#!/usr/bin/python3
''' List cities by state from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = "{}";'.format(sys.argv[4]))

    cities = cur.fetchall()
    print(", ".join([city[1] for city in cities]))

    cur.close()
    conn.close()
