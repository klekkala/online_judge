from settings import *
import MySQLdb as db
from user_profile import MyGlobals 

def index(req,start=0,user="%",show=10):
	try:
		start = int(start)
	except:
		start = 0
	try:
	 	show = int(show)-1
	except:
	 	show = 10
	conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	cursor.execute("select sid,username,problemid,status,score from submission where username like %sorder by sid desc",(user,))
	if start>0:
		cursor.fetchmany(start)
	temp_string = ""
	showing = 0
	for i in cursor:
		if showing > show:
			break
		showing+=1
		if i[3]=="Accepted":
			temp_string+= "<tr class=\"acc\">"
		else:
			temp_string+= "<tr class=\"nacc\">"
		temp_string+= "<td>"+str(i[0])+"</td>"
		MyGlobals.USER_NAME=str(i[1])
		temp_string+= "<td>"+str(i[1])+"</td>"
		temp_string+= "<td>"+str(i[2])+"</td>"
		temp_string+= "<td>"+str(i[3])+"</td>"
		temp_string+= "<td>"+str(i[4])+"</td>"
		temp_string+="</tr>"

	f = open(SYS_ROOT+"status_html.html").read()
	return f % (temp_string,)
