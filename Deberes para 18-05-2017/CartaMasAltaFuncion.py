#coding:utf-8

from random import randint
#Se definen las variables

salir=False


#########################################################################################
#					NIVEL 3																#
#########################################################################################
numero1= " "
numero2= " "
palo1= " "
palo2= " "

def figuras_j1():
	if (j1num >= 2 and j1num <= 10):
		numero1=j1num
	if (j1num ==11):
		numero1="J"
	if (j1num ==12):
		numero1="Q"
	if (j1num ==13):
		numero1="K"
	if (j1num ==14):
		numero1="A"
		
	return figuras_j1
	
def palos_j1():
	if (j1palo==1):
		palo1="Picas"
	if (j1palo==2):
		palo1="Trebol"
	if (j1palo==3):
		palo1="Diamantes"
	if (j1palo==4):
		palo1="Corazones"
		
	return palos_j1
	
def figuras_j2():
	if (j2num >= 2 and j2num <= 10):
		numero2=j2num
	if (j2num ==11):
		numero2="J"
	if (j2num ==12):
		numero2="Q"
	if (j2num ==13):
		numero2="K"
	if (j2num ==14):
		numero2="A"
		
	return figuras_j2
	
def palos_j2():
	if (j2palo==1):
		palo2="Picas"
	if (j2palo==2):
		palo2="Trebol"
	if (j2palo==3):
		palo2="Diamantes"
	if (j2palo==4):
		palo2="Corazones" 
	
	return palos_j2
	
################################################################################################
#					NIVEL 2																	   #
################################################################################################

def cartas_j1():
	figuras_j1()
	palos_j1()
	
def cartas_j2():
	figuras_j2()
	palos_j2()
	
def ganador(): 
	if (j1num > j2num):
		print "Gana J1"
	else:
		print "Gana J2"

################################################################################################
#					MAIN																	   #
################################################################################################

while (salir==False):
	j1num=randint(2,14)
	j1palo=randint(1,4)
	j2num=randint(2,14)
	j2palo=randint(1,4)
	cartas_j1()
	print "Jugador 1 tiene:", numero1 , "de" , palo1
	cartas_j2()
	print "Jugador 2 tiene:", numero2 , "de" , palo2
	ganador()
	if not ((j1num == j2num) and (j1palo == j2palo)):
		salir = True
