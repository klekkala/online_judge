from settings import *
import MySQLdb as db
#import cgi
#form = cgi.FieldStorage()
#abc = form.getvalue('id');
#abc = form['id'].value

abc= ""

"""f = open('test.txt')
lines = f.readlines()
abc = list(lines)
#is.strip('\'');
f.close()"""

class MyGlobals(object):
	    USER_NAME=""
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
	cursor.execute("select distinct problemid from submission where username like %s and status=\'Accepted\' order by sid desc",(abc,))
	if start>0:
		cursor.fetchmany(start)
	temp_string=abc
	showing = 0
	for i in cursor:
		if showing > show:
			break
		showing+=1
		temp_string+= "<td>"+str(i[0])+"</td>"
		temp_string+="</tr>"
	f = open(SYS_ROOT+"user_profile.html").read()
	return f % (temp_string,)
