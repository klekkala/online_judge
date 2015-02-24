#!/usr/bin/env python
# Main process

from settings import *
from rt_scripts import *
import MySQLdb as DB
from time import strptime,localtime,sleep,mktime

if __name__ == "__main__":
	stTime  = strptime(startTime,"%d %b %Y %H:%M")
	edTime  = strptime(endTime,"%d %b %Y %H:%M")
	while localtime() < stTime:
		diff = mktime(stTime) - mktime(localtime())
		print "Waiting for contest to start..."+str(diff)+" seconds to go"
		sleep(diff)
	while localtime() < edTime:
	#	sleep(3)
	        conn = DB.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
        	cursor = conn.cursor()
		if cursor.execute("select sid,problemid,language,program from submission where status like \"Queued...\"")!=0:
			record = cursor.fetchone()
			if cursor.execute("update submission set status=\"Assessing...\" where sid=%s",(record[0],))==1:
				print "Checking submission "+str(record[0])+" for problem "+record[1]+" in "+record[2]
				# Saving code in file
				filename = "currentCode."+LANG_EXT[LANG_NICK.index(record[2])]
				f = open(filename,"w")
				f.write(record[3])
				f.close()
				# Compile Code
				status,exename = compileCode(record[2],filename)
				if status == "OK":
					status,score = runCode(record[1],record[2],exename)
				else:
					score = 0
					status = "Compile Error"
				print "Result :"+status+"("+str(score)+")"
				cursor.execute("update submission set status=%s,score=%s where sid=%s",(status,int(score),record[0]))
		cursor.close()
		conn.commit()
		conn.close()
