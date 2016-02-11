#coding: utf-8
def my_range(inici, fi, increment):
	while inici <=fi:
		yield inici
		inici=inici + increment
		
for fil in my_range(1,8,1):
	for col in my_range(1,8,1):
		if (col%2==0 and fil%2==0):
			print "x",
		elif (col%2==1 and fil%2==1):
			print "x" ,
		else:
			print "o",
	print " "
