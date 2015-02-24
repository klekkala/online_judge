from settings import *
import MySQLdb as db

def index(req):
	conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	cursor.execute("select username,name from user")
	temp_string = ""
	count = 0
	for i in cursor:
		count+=1
		temp_string+= "<tr>"
		temp_string+= "<td>"+i[0]+"</td>"
		temp_string+= "<td text-align:left>"+i[1]+"</td>"
		temp_string+="</tr>"
	f = open(SYS_ROOT+"teamlist_html.html").read()
	return f % (temp_string,"<h2>Users Registered : "+str(count)+"</h2>")
