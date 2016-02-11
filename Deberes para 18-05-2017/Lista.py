#coding:utf-8
salir=False
salir_j1=False
salir_j2=False

from random import randint
#Crear la tabla con las 52 cartas disponibles
tabla= ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT", "AT", "2P", "3P", "4P", "5P", "6P", "7P", "8P", "9P", "10P", "JP", "QP", "KP", "AP", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"]



while (salir==False):
#Random jugador 1
	while (salir_j1==False):
		j1num=randint(2,14)
		j1palo=randint(1,4)
		
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
				
		if (j1palo==1):
			palo1="P"
		if (j1palo==2):
			palo1="T"
		if (j1palo==3):
			palo1="D"
		if (j1palo==4):
			palo1="C"
		print "Jugador 1 tiene:" ,numero1, "de" ,palo1
	
		if str(numero1)+palo1 in tabla:
			salir_j1=True
		
	tabla.pop(str(numero1) + palo1)
		
	
#Random jugador 2
	while (salir_j2==False):
		j2num=randint(2,14)
		j2palo=randint(1,4)
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
				
		if (j2palo==1):
			palo2="P"
		if (j2palo==2):
			palo2="T"
		if (j2palo==3):
			palo2="D"
		if (j2palo==4):
			palo2="C"
		print "Jugador 2 tiene:" ,numero2, "de" ,palo2

		if (str(numero2)+palo2 in tabla):
			salir_j2=True
	
	tabla.pop(str(numero2) + palo2)

	if (j1num==j2num):
		print empate
	else:
		if (j1num > j2num):
			print "Gana J1"
		else:
			print "Gana J2"
	
	raw_input("Dale a intro para continuar: ")
	
	if (len(tabla)==0):
		salir=True


