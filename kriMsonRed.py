from settings import *
import sys
import MySQLdb as db

def cmp(a,b):
	return 1 if a[2] <= b[2] else -1

def prob_sort(a, b):
	return -1 if int(a[1:]) < int(b[1:]) else 1


def index(req):
	conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	cursor.execute("select username,problemid,score from submission where score>0 and username!='test' and username!='admin'")
	mp = {}
	for i in cursor:
		if mp.has_key(i[0]):
			if mp[i[0]].has_key(i[1]):
				mp[i[0]][i[1]] = max( mp[i[0]][i[1]], i[2])
			else:
				mp[i[0]][i[1]] = i[2]
		else:
			mp[i[0]] = {}
			mp[i[0]][i[1]] = i[2]
	temp_list = []
	for i in mp.iterkeys():
		user = i
		solved = []
		score = 0
		for j in mp[i].iterkeys():
			solved.append(j)
			score+=mp[i][j]
			solved.sort(cmp=prob_sort)
		temp_list.append((user,", ".join(solved),score))

	#sys.stderr.write(
	#		str(temp_list) + '\n'*10 + str(type(temp_list[0][2])))

	temp_list.sort(cmp=cmp)
	temp_string = " "
	for num,i in enumerate(temp_list):
	  	temp_string+="<tr>"
		temp_string+="<td>"+str(num+1)+"</td>"
		temp_string+="<td>"+str(i[0])+"</td>"
		temp_string+="<td>"+str( 
								i[1]
								#sorted(i[1].split('+'))
								)+"</td>"
		temp_string+="<td>"+str(i[2])+"</td>"
		temp_string+="</tr>"
	f = open(SYS_ROOT+"ranklist.html").read()
	return f % (temp_string,)
