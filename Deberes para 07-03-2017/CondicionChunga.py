#coding: UTF8
#!/bin/bash

Numero = input("Introduce un numero porfavor: ")

if Numero%2 == 0:
	print "Este numero es par"
	
if (Numero >= -10) and (Numero <= 40):
	print "Este numero esta entre -10 y 40"
	
if Numero < 0:
	print "Este numero es negativo"
