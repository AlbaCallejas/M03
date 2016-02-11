#coding: utf-8
#Menu de una calculadora
#Hecho por Alba Callejas

import time

import os


while True:
	os.system('clear')
	print "Menu de una calculadora:"
	time.sleep (2)
	print
	print "==============="
	print "1-Sumar"
	print "2-Restar"
	print "3-Multiplicar"
	print "4-Dividir"
	print "5-Salir"
	print "==============="
	print
	time.sleep (1)
	numero= input("¿Que desea hacer el amo?: ")
	time.sleep (1)
	if (numero == 1):
		print "Has seleccionado la opción de Sumar!"
	elif (numero == 2):
		print "Has seleccionado la opción de Restar!"
	elif (numero == 3):
		print "Has seleccionado la opción de Multiplicar!"
	elif (numero == 4):
		print "Has seleccionado la opción de Dividir!"
	elif (numero == 5):
		print "Adios!"
		break
	else:
		print "Esta opción no existe!"
	time.sleep (3)
	 
