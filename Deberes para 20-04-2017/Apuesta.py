# coding:utf-8
# Les cartes tenen un nº: A,2-10,J,Q,K (total 13)
# Les cartes tenen un pal: cors, piques, trebols, diamants (total de 4)
import time
from random import randint

j1num=randint(2,14)
j1pal=randint(1,4)
j2num=randint(2,14)
j2pal=randint(1,4)

salir= False
salir_apuesta = False
saldo=100
apuesta_minima=10

while (salir_apuesta == False):
	print ("Tu saldo actual es de: "), saldo
	apuesta=input("Introduce tu apuesta, -1 para retirarse: ")
		
	if (saldo < apuesta_minima):
		print ("Lo siento! No tienes suficiente dinero!")
		time.sleep(1)
		salir = True
		salir_apuesta = True
	else:
		if ((apuesta >= apuesta_minima) and (apuesta <= saldo)):
			salir_apuesta= True
			saldo= saldo - apuesta
		else:
			if (apuesta == -1):
				print ("Bye-Bye!")
				salir =True
				salir_apuesta = True
			else:
				print ("Apuesta no valida!")
		 
while ((salir == False) and (salir_apuesta == True)):
	print ("Tu saldo actual es de: "), saldo
	# Generem tirada del jugador 1	
	j1num=randint(2,14)
	j1pal=randint(1,4)

	numero=j1num
	if (j1num==11):
		numero="J"
	if (j1num==12):
		numero="Q"
	if (j1num==13):
		numero="K"
	if (j2num==14):
		numero="A"

	if (j1pal==1):
		pal="Picas"
	if (j1pal==2):
		pal="Treboles"
	if (j1pal==3):
		pal="Diamantes"
	if (j1pal==4):
		pal="Corazones"

	print "BANCA te: " , numero, "de " , pal

	# Generem la tirada de jugador2 (agafa una carta aleatoria)
	
	j2num=randint(2,14)
	j2pal=randint(1,4)

	numero=j2num
	if (j2num==11):
		numero="J"
	if (j2num==12):
		numero="Q"
	if (j2num==13):
		numero="K"
	if (j2num==14):
		numero="A"

	if (j2pal==1):
		pal="P"
	if (j2pal==2):
		pal="T"
	if (j2pal==3):
		pal="D"
	if (j2pal==4):
		pal="C"

	print "Jugador te: " , numero, "de " , pal

	# Comprovem si hi ha empat
	if (j1num==j2num):
		print "Empat"
	else:
		if (j2num>j1num):
			print "Guanya Jugador"
			saldo= saldo + (apuesta * 2)
		else:
			print "Guanya BANCA"
			
	if ((saldo < 10) or (apuesta == -1)):
		salir =True
	else:
		print ("Tu saldo actual es de: "), saldo
		apuesta=input("Introduce tu apuesta, -1 para retirarse: ")

		if (saldo < apuesta_minima):
			print ("Lo siento! No tienes suficiente dinero!")
			time.sleep(1)
			salir = True
			salir_apuesta = True
		else:
			if ((apuesta >= apuesta_minima) and (apuesta <= saldo)):
				salir_apuesta= True
				saldo= saldo - apuesta
			else:
				if (apuesta == -1):
					print ("Bye-Bye!")
					salir = True
					salir_apuesta = True
				else:
					print ("Apuesta no valida!")
					salir = True
					
		
	

