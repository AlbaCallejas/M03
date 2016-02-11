#coding: utf-8
def my_range(inici, fi, increment):
	while inici <=fi:
		yield inici
		inici=inici + increment
		
for fila in my_range(1,5,1):
	for columna in my_range(1,4,1):
		if (fila==1):
			if (columna==2):
				print "A",
				
			elif (columna==3):
				  print "B",
				  
			elif (columna==4):
				  print "C",
				  
			else:
				  print "-"
		
		else:
			
			if (columna==1):
				  print fila -1 ,
			else:	  
				
				if ( (fila==3 and columna==2) or (fila==2 and columna==3) ):
					print "*" ,
				else:
					print "-" ,
						
	print ""
						
						
						
