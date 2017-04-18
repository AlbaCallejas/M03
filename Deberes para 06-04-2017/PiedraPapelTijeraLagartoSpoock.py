# coding:utf-8
# Possibilitats: PE, PA, TI, LA, SP
# Total 9: 3 empat, 6 guanyador
# jugador1 humà
# jugador2 machine

import os
from random import randint
os.system('clear')
# Jugador humà
jugador1=raw_input("Possi la jugada (PI/PA/TI/LA/SP):")

# Jugador machine
aleatori=randint(1,5)
if (aleatori==1):
	jugador2="PI"
if (aleatori==2):
	jugador2="PA"
if (aleatori==3):
	jugador2="TI"
if (aleatori==4):
	jugador2="LA"
if (aleatori==5):
	jugador2="SP"

# Empat (3 combinacions)
if (jugador1==jugador2):
	print "Empat"
else: # 6 combinacions
	# Guanya jugador1 (3 combinacions)
	if (((jugador1=="PI") and (jugador2=="TI" or jugador2=="LA")) or
	    ((jugador1=="PA") and (jugador2=="PI" or jugador2=="SP")) or 
	    ((jugador1=="TI") and (jugador2=="PA" or jugador2=="LA")) or 
	    ((jugador1=="LA") and (jugador2=="PA" or jugador2=="SP")) or
	    ((jugador1=="SP") and (jugador2=="PI" or jugador2=="TI"))):
	   
		print "Tu guanyes!!!!!"
	else: # Guanya jugador2 (3 combinacions)
		print "Ets un .... has perdut !!!!"
