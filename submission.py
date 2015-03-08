from settings import *
import MySQLdb as DB
from mod_python import util
from time import localtime
from datetime import datetime,timedelta

def index(req,username,passwd,pid,lang,upload):
	if type(upload) == type(" "):
		ERROR = "Path specified doesn't point to a valid file."
	else:
	 	verdict = 0
	 	count = 1
		ERROR = "ERROR: Our server is facing some problem, please retry after few minutes."
		conn = DB.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
		cursor = conn.cursor()
		try:
			cursor.execute("""select password from user where username=%s""",(username,))
			record = cursor.fetchone()
			if not record:
				ERROR = "Sorry, no username is registered with this name."
				verdict = 1
		except:
		  	pass
		if verdict == 0:
			if passwd != record[0]:
				ERROR = "Wrong password."
				verdict = 1
		try:
			cursor.execute("""select count,time from submission where problemid=%s and username=%sorder by count desc""",(str(pid),username))
			record = cursor.fetchone()
			if record:
				subAll = MAX_SUBMISSION[ PROBLEMS_ID.index(pid) ]
				if record[0] == subAll:
					verdict = 1
					ERROR = "You have already used all your chances for "+pid
				if datetime.timetuple(record[1]+timedelta(seconds=TIME_DIFF)) > localtime():
					verdict = 1
					ERROR = "Minimum gap between submissions for same problem is "+str(TIME_DIFF)+" secs, please wait"
				count = record[0]+1
		except:
			return "ERROR"
		if verdict == 0:
			try:
				cursor.execute("""insert into submission(username,problemid,language,count,program) values(%s,%s,%s,%s,%s)""",(username,pid,lang,count,upload.value))
				cursor.close()
				conn.commit()
				conn.close()
				##exec("python ../eval/worker.py") 
				return util.redirect(req,"status.py")
			except:
				pass
		cursor.close()
		conn.commit()
		conn.close()
	probList = ""
	for i in PROBLEMS_ID:
		probList+="<option value=\"%s\">%s</option>"%(i,i)
	langList = ""
	for i,j in zip(LANGUAGES,LANG_NICK):
		langList+="<option value=\"%s\">%s</option>"%(j,i)
	f = open(SYS_ROOT+"submission.html").read()
	return f % ("<h2>"+str(ERROR)+"</h2>",probList,langList)
