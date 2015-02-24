from settings import *
from time import localtime,strptime

def index(req):
        stTime  = strptime(startTime,"%d %b %Y %H:%M")
        edTime  = strptime(endTime,"%d %b %Y %H:%M")
	probList = ""
	if localtime() >= stTime and localtime() <= edTime:
		for i in PROBLEMS_ID:
			probList+="<option value=\"%s\">%s</option>"%(i,i)
		langList = ""
		for i,j in zip(LANGUAGES,LANG_NICK):
			langList+="<option value=\"%s\">%s</option>"%(j,i)
		f = open(SYS_ROOT+"submission.html").read()
		return f % ("",probList,langList)
	elif localtime() < stTime:
		f = open(SYS_ROOT+"announcements.html").read()
		temp_string = "<h2>The contest has not yet started.</h2>"
	else:
		f = open(SYS_ROOT+"announcements.html").read()
		temp_string = "--> <h2>The deadline has ended.</h2> <!--"
	return f % (temp_string,)
