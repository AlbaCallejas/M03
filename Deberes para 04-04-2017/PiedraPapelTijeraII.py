#coding:utf-8

import os
#Variables
salir= False
num=31
J1=31
J2=31

while (salir==False):
	#Se definen las opciones
	if (J1%7==0) or (J1%7==1):
		print num,("J1: Tijera")
	else:
		if (J1%7==2) or (J1%7==3) or (J1%7==6):
			print num,("J1: Piedra")
		else:
			if (J1%7==4) or (J1%7==5):
				print num,("J1: Papel")
		
	if (J2%5==0) or (J2%5==1):
		print num,("J2: Papel")
	else:
		if (J2%5==2) or (J2%5==3):
			print num,("J2: Tijera")
		else:
			if (J2%5==4):
				print num,("J2: Piedra")
	
	print
################# Hay un ganador#####################################################
	if ( (J1%7==2) or (J1%7==3) or (J1%7==6)) and ((J2%5==0) or (J2%5==1)):
		print ("J2 WINS!")
	else:
		if ( (J1%7==2) or (J1%7==3) or (J1%7==6)) and ((J2%5==2) or (J2%5==3)):
			print ("J1 WINS!")
		else:
			if ( (J1%7==0) or (J1%7==1)) and ((J2%5==0) or (J2%5==1)):
				print ("J1 WINS!")
			else:
				if ( (J1%7==0) or (J1%7==1)) and (J2%5==4):
					print ("J2 WINS!")
				else:
					if ( (J1%7==4) or (J1%7==5)) and ((J2%5==2) or (J2%5==3)):
						print ("J2 WINS!")
					else:	
						if ( (J1%7==4) or (J1%7==5)) and (J2%5==4):
							print ("J1 WINS!")
	
################# Hay empate ########################################################
	if ((J1%7==0) or (J1%7==1)) and ((J2%5==2) or (J2%5==3)):
		print ("Empate!!!")
	else:
		if ((J1%7==2) or (J1%7==3) or (J1%7==6)) and ((J2%5==4)):
			print ("Empate!!!")
		else:
			if ((J1%7==4) or (J1%7==5)) and ((J2%5==0) or (J2%5==1)):
				print ("Empate!!!")
	print
####### Condicion de salida ########################################################
	if (num==57):
		salir = True
	num=num+1
	J1=J1+1
	J2=J2+1

	

