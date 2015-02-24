from settings import *
from time import localtime,strptime
import os
def index(req):
	num = len(PROBLEMS_ID)
	temp_string = ""
        stTime  = strptime(startTime,"%d %b %Y %H:%M")
        edTime  = strptime(endTime,"%d %b %Y %H:%M")
	f = ""
	if localtime() >= stTime and localtime() <= edTime:
		for i in xrange(num):
			temp_string+= "<tr>"
			temp_string+= "<td>"+PROBLEMS_ID[i]+"</td>"
			temp_string+= "<td><a href=\"%s\">%s</a></td>" % (PROBLEMS_PAGE[i],PROBLEMS_NAME[i])
			temp_string+= "<td>"+str(PROBLEMS_SCORE[i])+"</td>"
			temp_string+= "<td>"+str(MAX_SUBMISSION[i])+"</td>"
			temp_string+="</tr>"
		f = open(SYS_ROOT+"problems.html").read()
	elif localtime() < stTime:
		f = open(SYS_ROOT+"announcements.html").read()
		temp_string = "--> <h2>The contest has not yet started.</h2> <!--"
	else:
		f = open(SYS_ROOT+"announcements.html").read()
		temp_string = "--> <h2>The contest has ended.</h2> <!--"
	return f % (temp_string,)
