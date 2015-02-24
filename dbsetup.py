#!/usr/bin/env python
from settings import *
import MySQLdb as db

conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
cursor = conn.cursor()
try:
	cursor.execute("drop table user")
except:
	pass

try:
	cursor.execute("drop table submission")
except:
	pass
cursor.execute("create table user (username CHAR(255) PRIMARY KEY NOT NULL, password CHAR(255), name CHAR(255), email CHAR(255) UNIQUE)")
cursor.execute("create table submission (sid INT PRIMARY KEY AUTO_INCREMENT,username CHAR(255), problemid CHAR(32), language CHAR(16), count INT, time TIMESTAMP, status char(255) default 'Queued...', program blob, score INT default 0)")
cursor.close()
conn.commit()
conn.close()
