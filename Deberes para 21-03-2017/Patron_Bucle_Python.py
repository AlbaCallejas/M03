#coding: utf-8
#Patrón para hacer bucles en python

salir = False

while (salir == False): 
	print ("Hola")
	tecla= raw_input("Introduce un caracter: ")
	
	if (tecla == "S" or tecla == "s" ):
		print ("Adiós")
	else: 
		salir = True


