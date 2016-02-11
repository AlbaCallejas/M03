#coding:utf-8

import os
from random import randint
os.system('clear')

	###CARTAS CPU 1:###
numeroCPU1=randint(1,13)

if (numeroCPU1==1): 
	CPU1=1
if (numeroCPU1==2):
	CPU1=2
if (numeroCPU1==3):
	CPU1=3
if (numeroCPU1==4):
	CPU1=4
if (numeroCPU1==5):
	CPU1=5
if (numeroCPU1==6):
	CPU1=6
if (numeroCPU1==7):
	CPU1=7
if (numeroCPU1==8):
	CPU1=8
if (numeroCPU1==9):
	CPU1=9  
if (numeroCPU1==10):
	CPU1=10 
if (numeroCPU1==11):
	CPU1="J"
if (numeroCPU1==12):
	CPU1="Q"
if (numeroCPU1==13):
	CPU1="K"
###FIN DE CARTAS CPU 1###
	
###TIPO CARTAS CPU 1###

tipo=randint(1,4)

if (tipo==1):
	tipoCPU1="Picas"
if (tipo==2):
	tipoCPU1="Diamantes"
if (tipo==3):
	tipoCPU1="Trebol"
if (tipo==4):
	tipoCPU1="Corazones" 
###FIN DE TIPO CARTAS CPU 1###

print "CPU1: Tengo un ", CPU1 , "de" , tipoCPU1

	### CARTAS CPU 2###
numeroCPU2=randint(1,13)

if (numeroCPU2==1): 
	CPU2=1
if (numeroCPU2==2):
	CPU2=2
if (numeroCPU2==3):
	CPU2=3
if (numeroCPU2==4):
	CPU2=4
if (numeroCPU2==5):
	CPU2=5
if (numeroCPU2==6):
	CPU2=6
if (numeroCPU2==7):
	CPU2=7
if (numeroCPU2==8):
	CPU2=8
if (numeroCPU2==9):
	CPU2=9  
if (numeroCPU2==10):
	CPU2=10 
if (numeroCPU2==11):
	CPU2="J"
if (numeroCPU2==12):
	CPU2="Q"
if (numeroCPU2==13):
	CPU2="K"
	
###FIN DE CARTAS CPU 2###

###TIPO CARTAS CPU 2###

tipo2=randint(1,4)

if (tipo2==1):
	tipoCPU2="Picas"
if (tipo2==2):
	tipoCPU2="Diamantes"
if (tipo2==3):
	tipoCPU2="Trebol"
if (tipo2==4):
	tipoCPU2="Corazones" 


###FIN DE TIPO CARTAS CPU 2###

print "CPU2: Tengo un ", CPU2 , "de" , tipoCPU2

###Empate###

if (numeroCPU1==numeroCPU2):
	print "Empate!!"


###Ganador###

if (numeroCPU1 > numeroCPU2):
	print "Gana CPU1!!!"
else:
	print "Gana CPU2!!!"
	





























