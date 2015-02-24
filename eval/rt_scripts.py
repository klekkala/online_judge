# Contains code for compiling and executing codes using sandbox.
from settings import *
from problems import *
import os
from subprocess import *
def compileCode(lang,filename):  # Code is in 'current.???' according to language used.
	if lang == "CPP":
		exit_code = os.system("g++ -O2 -s -static -o current.out "+filename)
		if exit_code != 0:
			return "ERROR",""
	if lang == "C":
		exit_code = os.system("gcc -O2 -s -static -o current.out "+filename+" -lm")
		if exit_code != 0:
			return "ERROR",""
	if lang =="JAVA":
		exit_code = os.system("gcj --main=Main    -o current.out "+filename)
		if exit_code !=0:
			return "ERROR",""
	if lang =="PAS":
		pass
	return "OK","current.out"
def runCode(pid,lang,exename):       # Executable is in corresponding file as generated in compileCode
	score = 0
	timeFactor = TIME_FACTOR [ LANG_NICK.index(lang) ]
	for test in testcases[pid]:
		try:
			infile = TEST_ROOT+test[0]
			outfile = TEST_ROOT+test[1]
			#cmd = "./sandbox.out -a2 -f -m %d -t %d -i %s -o %s %s" % (test[3]*1024,test[4]*timeFactor,infile,"temp.out",exename)
			cmd = "./box.out -a1 -f -m %d -t %d -i %s -o %s %s" % (test[3]*1024,test[4]*timeFactor,infile,"temp.out",exename)
			print cmd
			p = Popen(cmd,shell=True,stdout=PIPE,stderr=STDOUT,close_fds=True)
			p.wait()
			status = p.stdout.read().strip().split('\n')[0]
			print "For test case %s got status %s" % (test[0],status)
			if status.split(' ')[0] == "OK":
				cmd = "./%s %s %s" % (checker[pid],outfile,"temp.out")
				print cmd
				p = Popen(cmd,close_fds=True,shell=True)
				if p.wait()==0:
					score+=test[2]
				else:
					return "Wrong Answer",score		
			else:
				if status.split(' ')[0]=="Caught":
					return "SegFault",score
				return status,score
		except:
			return "UnKnown Error",score
	return "Accepted",score
