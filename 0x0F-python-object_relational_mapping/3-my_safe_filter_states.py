#!/usr/bin/bash
''' Take in arguments and display all values in the states table
from the database hbtn_0e_0_usa where name matches the argument
'''
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
    cur.execute('SELECT * FROM states WHERE name = (%s) \
        ORDER BY states.id ASC', (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    conn.close()
