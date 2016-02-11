#coding:utf-8

from random import randint
#Se definen las variables
j1num=randint(2,14)
j1palo=randint(1,4)
salir=False

while (salir==False):
	#Se definen el numero/letra de cada carta del jugador 1
	if (j1num >= 2 and j1num <= 10):
		numero=j1num

	if (j1num ==11):
		numero="J"
	if (j1num ==12):
		numero="Q"
	if (j1num ==13):
		numero="K"
	if (j1num ==14):
		numero="A"
		
	if (j1palo==1):
		palo="Picas"
	if (j1palo==2):
		palo="Trebol"
	if (j1palo==3):
		palo="Diamantes"
	if (j1palo==4):
		palo="Corazones" 
	print "Jugador 1 tiene:" ,numero, "de" ,palo

	
	
	j2num=randint(2,14)
	j2palo=randint(1,4)
	
	#Se definen el numero/letra de cada carta del jugador 2
	if (j2num >= 2 and j2num <= 10):
		numero=j2num

	if (j2num ==11):
		numero="J"
	if (j2num ==12):
		numero="Q"
	if (j2num ==13):
		numero="K"
	if (j2num ==14):
		numero="A"
		
	if (j2palo==1):
		palo="Picas"
	if (j2palo==2):
		palo="Trebol"
	if (j2palo==3):
		palo="Diamantes"
	if (j2palo==4):
		palo="Corazones" 
	print "Jugador 2 tiene:" ,numero, "de" ,palo

	#Ganadores
	if (j1num > j2num):
		print "Gana J1"
	else:
		print "Gana J2"
	#Condicion de salida
	if not ((j1num == j2num) and (j1palo == j2palo)):
		salir = True









