from settings import *
from time import localtime,strptime
import MySQLdb as DB
from mod_python import util,apache

def index(req):
	rgTime  = strptime(regTime,"%d %b %Y %H:%M")
	if localtime() <= rgTime:
		f = open(SYS_ROOT+"register_form.html")
		text = f.read() % ("")
		f.close()
		return text
	else:
		f = open(SYS_ROOT+"announcements.html").read()
		temp_string = "--> <h2>The registeration is closed.</h2> <!--"
		return f % (temp_string,)
