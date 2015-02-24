# Contains information about test data for problems

TEST_ROOT = "/var/www/html/eval/exam/"   # The location where test cases input/output files are located on your system. Absolute Path.

# 'testcases' should map problemID to a list of test cases.
# Each test case is a tuple in following format.
# ( inputFilename, outputfilename, score, memory limit in MBs, time limit in secs)

testcases = {
	"P1" : [ ("in1_1","out1_1",25,32,1),("in1_2","out1_2",25,32,1),("in1_3","out1_3",25,32,1),("in1_4","out1_4",25,32,1)],

	"P2" : [ ("in2","out2",100,8,1) ],

	"P3" : [ ("in3","out3",100,32,1) ],
	"P4" : [ ("in4_1","out4_1",50,32,2),("in4_2","out4_2",50,32,2)],
}

# 'checker' should map problemID to a program name that is to be used to check out.
# You can code checker as per your need. They are simple C/CPP programs that take as argument two filenames locally available.
# The first file is, JUDGE output and second is contestant solution. If your problem has no JUDGE output, use a empty file and dont use it latter on.
# The program as its exit code ( return '0' / return '1' ) should return verdict as correct (0) or wrong (!0).
#
# By default, we provide a simple checker, exact.out that checks character by character.

checker  = {"P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out"}
