#coding:UTF8
#!/bin/bash

#Usuario pone su edad
edad = input("Introduce tu edad: ")

#Depende de la edad, te muestra un mensaje diferente
if (edad >=18 and edad <=23) or (edad == 17):
	print "Puedes pasar a la sesión de jovenes"

elif (edad >= 65):
	print "Que haces aqui? Eres demasiado mayor!!"

elif (edad >=24 and edad <=64): 
	print "Disculpe...Pero esta cerrado..."

elif (edad <17):
	print "Venga niño vuelve a casa para merendar"
