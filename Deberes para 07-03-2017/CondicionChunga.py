#coding: UTF8
#!/bin/bash

#Usuario pone un numero
Numero = input("Introduce un numero porfavor: ")

#Numero par
if Numero%2 == 0:
	print "Este numero es par"
#Numero en un rango	
if (Numero >= -10) and (Numero <= 40):
	print "Este numero esta entre -10 y 40"
#Numero impar	
if Numero < 0:
	print "Este numero es negativo"
