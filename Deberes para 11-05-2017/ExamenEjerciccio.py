#coding: utf-8
def my_range(inici, fi, increment):
	while inici <=fi:
		yield inici
		inici=inici + increment
		
for fil in my_range(1,4,1):
	for col in my_range(1,8,1):
		if (fil==1 or fil==4):
			print "*",
		else:
			if (col==1 or col==8):
				print "*",
			elif (fil==2 and col==3):
				  print "H",
			elif (fil==2 and col==4):
				  print "O",
			elif (fil==2 and col==5):
				  print "L",
			elif (fil==2 and col==6):
				  print "A",
				 	
	print " " 
		
