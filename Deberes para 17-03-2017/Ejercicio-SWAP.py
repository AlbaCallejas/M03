#coding: utf-8
#Ejercicio SWAP
#Hecho por Alba Callejas

import time

mano_der = "Movil"
mano_izq = "Bocata"
mano_extra = "Aire"

print "En la derecha tengo",mano_der
print "En la izquierda tengo",mano_izq

time.sleep (3)
print "Se esta produciendo un cambio de objetos!"
mano_extra = mano_der
mano_der = mano_izq
mano_izq = mano_extra 

time.sleep (2)
print "En la derecha tengo",mano_der
print "En la izquierda tengo",mano_izq
