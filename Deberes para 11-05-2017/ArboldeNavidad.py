#coding: utf-8
def my_range(inici, fi, increment):
	while inici <=fi:
		yield inici
		inici=inici + increment
		
for fil in my_range(1,6,1):
	for col in my_range(1,5,1):
		if (fil==4):
			print "A" ,
		else:
			if (fil==3):
				if (col==fil or col%2==0):
					print "A",
			else:
				if (col==3):
					if (fil==1):
						print "*",
					elif (fil==2):
						  print "A",
					elif (fil==5 or fil==6):
						  print "N",
					else:
						print " " ,
	print " "
