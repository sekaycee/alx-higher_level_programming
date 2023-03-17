#!/usr/bin/python3
''' List cities by state from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    #cur.execute('SELECT cities.name FROM cities WHERE state_id \
    #        IN (SELECT states.id FROM states WHERE states.name = "{}") \
    #        ORDER BY cities.id ASC'.format(sys.argv[4]))
    cur.execute('SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name LIKE BINARY (%s) ORDER BY cities.id ASC',
                 (sys.argv[4]))

    cities = cur.fetchall()
    #print(', '.join([city for city in cities]))
    end_str = ""
    str_cities = ""
    for row in table:
        str_cities = str_cities + end_str + row[0]
        end_str = ", "

    print(str_cities)

    cur.close()
    conn.close()
