#coding: utf-8
#Menu de una calculadora v.2
#Hecho por Alba Callejas

import time

import os

ON = True

while (ON == True):
	os.system('clear')
	print "Menu de una calculadora:"
	time.sleep (2)
	print
	print "==============="
	print "1-Sumar"
	print "2-Restar"
	print "3-Multiplicar"
	print "4-Dividir"
	print "S-Salir"
	print "==============="
	print
	time.sleep (1)
	numero= raw_input("¿Que desea hacer el amo?: ")
	time.sleep (1)
	if (numero == "1"):
		print "Has seleccionado la opción de Sumar!"
	elif (numero == "2"):
		print "Has seleccionado la opción de Restar!"
	elif (numero == "3"):
		print "Has seleccionado la opción de Multiplicar!"
	elif (numero == "4"):
		print "Has seleccionado la opción de Dividir!"
	elif (numero == "S" or numero == "s"):
		print "Adios!"
		time.sleep (1)
		ON = False
	else:
		print "Esta opción no existe!"
	time.sleep (3)
	 
