#from settings import *
import os
import shutil
import sys
import MySQLdb as db

def cmp(a,b):
	return 1 if a[2] <= b[2] else -1

def prob_sort(a, b):
	return -1 if int(a[1:]) < int(b[1:]) else 1

MYSQL_HOST = 'localhost'
MYSQL_PASS = 'ravi@1234'
MYSQL_USER = 'root'
MYSQL_DB = 'oj'

PROBLEM = str(sys.argv[1])

conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
cursor = conn.cursor()
cursor.execute("select username,problemid,score,program,sid from submission where score>0 and username!='test' and username!='admin' and problemid='%s'" % PROBLEM)
mp = {}
codes = {}
for i in cursor:
	if mp.has_key(i[0]):
		if mp[i[0]].has_key(i[1]):
			if mp[i[0]][i[1]][0] <= i[2] and mp[i[0]][i[1]][2] < i[4]:
				mp[i[0]][i[1]] = (i[2], i[3], i[4])
		else:
			mp[i[0]][i[1]] = (i[2], i[3], i[4])
	else:
		mp[i[0]] = {}
		mp[i[0]][i[1]] = (i[2], i[3], i[4])


"""
	{ uid: {pid : (score, code, timestamp)} }
"""

## Generic
#for i in mp.keys():
#	for j in mp[i].keys():
#		with open("%s_%s.c" % (i, j), "w") as f:
#			f.write(str(mp[i][j][1]))

if os.path.isdir(PROBLEM):
	shutil.rmtree(PROBLEM)
os.mkdir(PROBLEM)
for i in mp.keys():
	with open(os.path.join(PROBLEM, "%s.c" % (i)), "w") as f:
		f.write(str(mp[i][PROBLEM][1]))
