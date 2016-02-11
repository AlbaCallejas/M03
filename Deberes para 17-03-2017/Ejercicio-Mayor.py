#coding: utf-8
#Ejercicio-Mayor
#Hecho por Alba Callejas

valor1 =input("Introduzca un valor: ")
valor2 =input("Introduzca otro valor: ")

if ( valor1 > valor2 ):
	print "El valor" ,valor1, "es mayor!"
else:
	if ( valor1 < valor2 ):
		print "El valor" ,valor2, "es mayor!"
	else:
		print "Los valores son iguales!"
