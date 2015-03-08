from settings import *
import MySQLdb as DB
from mod_python import util
import uuid
string = str(uuid.uuid4())
def index(req,username,name,email):
	conn = DB.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	try:
		cursor.execute("""insert into user(username,password,name,email) values(%s,%s,%s,%s)""",(username,string,name,email))
		cursor.close()
		conn.commit()
		conn.close()
		f = open(SYS_ROOT+"register_form.html")
		text1 = f.read() % (" --><h2>"+string+"</h2><!-- ")
		f.close()
		return text1
	except:
		pass
	cursor.close()
	conn.commit()
	conn.close()
	f = open(SYS_ROOT+"register_form.html")
	text = f.read() % (" --><h2>ERROR: Someone else is already using this Username/E-mail ID</h2><!-- ")
	f.close()
	return text
