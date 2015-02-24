#!/usr/bin/env python
from settings import *
import sys
import MySQLdb as db

if __name__ == "__main__":

	rollnumber = sys.argv[0]
	#input <roll number>, output is in <rollnumber>.txt
	conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db='oj2')
	cursor = conn.cursor()

	# write the command here using rollnumber
	cmd = "select program from submission where username=201381035 and problemid='P3';"

	cursor.execute(cmd)

	fo = open(str(rollnumber)+".txt","w")
	fo.write(cursor.fetchall())
	fo.close()

	cursor.close()
	conn.commit()
	conn.close()


