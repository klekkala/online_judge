from settings import *
import MySQLdb as db

PROBLEMS_ID = ["P1","P2","P3","P4","P5","P6","P7","P8"]
def index(req):
	string = ""
	conn = db.connect(host=MYSQL_HOST,passwd=MYSQL_PASS,user=MYSQL_USER,db=MYSQL_DB)
	cursor = conn.cursor()
	cursor.execute("select sid,username,problemid,status,mem,time from submission")
	j = 0
	count_tot = {'P1':0.00,'P2':0.00,'P3':0.00,'P4':0.00,'P5':0.00,'P6':0.00,'P7':0.00,'P8':0.00}
	count_acc = {'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
	count_tle = {'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
	count_wans = {'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
	count_segf = {'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
	count_cerr = {'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
 	
	
	for i in cursor:
		count_tot[i[2]] = count_tot[i[2]] + 1
		if i[3] =="Accepted":
			count_acc[i[2]] = count_acc[i[2]] + 1
		elif i[3] =="Wrong Answer":
			count_wans[i[2]] = count_wans[i[2]] + 1
		elif i[3] =="Time limit exceeded":
			count_tle[i[2]] = count_tle[i[2]] + 1
		elif i[3] =="SegFault":
			count_segf[i[2]] = count_segf[i[2]] + 1
		elif i[3] =="Compile Error":
			count_cerr[i[2]] = count_cerr[i[2]] + 1

	while j <= 7:
		string += "<td><b>" + str(j)+"</td>"
		string += "<td><b>" + PROBLEMS_ID[j] + "</td>"
		string += "<td><b>" + '100'+"</td>"
		string += "<td><b>" + str(count_acc[PROBLEMS_ID[j]])+"</td>"
		string += "<td><b>" + str(count_segf[PROBLEMS_ID[j]])+"</td>"
		string += "<td><b>" + str(count_tle[PROBLEMS_ID[j]])+"</td>"
		string += "<td><b>" + str(count_wans[PROBLEMS_ID[j]])+"</td>"
		string += "<td><b>" + str(count_cerr[PROBLEMS_ID[j]])+"</td>"

		try:
			value = count_acc[PROBLEMS_ID[j]]/count_tot[PROBLEMS_ID[j]]
		except ZeroDivisionError:
			value = 0.00
		else:
			value = count_acc[PROBLEMS_ID[j]]/count_tot[PROBLEMS_ID[j]]

		string += "<td><b>" + str(value)+"</td>"
		string += "<td><b>" + str(value)+"</td>"
		string += "<td><b>" + str(value)+"</td>"
		string +="</tr>"
		j = j+1
	f = open(SYS_ROOT+"dashboard.html").read()
	return f % (string,)

	
		
		
