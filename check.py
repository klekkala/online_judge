from settings import *
import MySQLdb as DB
from mod_python import util

def index(req,username,passwd,name,email):
	conn = DB.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	try:
		cursor.execute("""insert into user(username,password,name,email) values(%s,%s,%s,%s)""",(username,passwd,name,email))
		cursor.close()
		conn.commit()
		conn.close()
		return util.redirect(req,"teamlist.py")
	except:
		pass
	cursor.close()
	conn.commit()
	conn.close()
	f = open(SYS_ROOT+"register_form.html")
	text = f.read() % (" --><h2>ERROR: Someone else is already using this Username/E-mail ID</h2><!-- ")
	f.close()
	return text
