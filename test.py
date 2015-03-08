import os
from subprocess import *
cmd = './box.out -a1 -f -m 32768 -t 1 -i /var/www/html/eval/exam-2/in1 -o temp.out current.out'
#print cmd
p = Popen(cmd,shell=True,stdout=PIPE,stderr=STDOUT,close_fds=True)
p.wait()
status = p.stdout.read().strip().split('\n')[0]
print status.split(' ')[0]
