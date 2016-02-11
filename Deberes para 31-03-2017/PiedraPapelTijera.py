#coding: utf-8

import os
import time

os.system('clear')
J1=raw_input("Jugador 1: Piedra, papel o tijera?: ")
time.sleep (1)
print
J2=raw_input("Jugador 2: Piedra, papel o tijera?: ")
time.sleep (1)
print

if ( J1 == "piedra" and J2 == "papel"):
	print ("J2 WINS!")
if ( J1 == "piedra" and J2 == "tijera"):
	print ("J1 WINS!")
if ( J1 == "tijera" and J2 == "papel"):
	print ("J1 WINS!")
if ( J1 == "tijera" and J2 == "piedra"):
	print ("J2 WINS!")
if ( J1 == "papel" and J2 == "tijera"):
	print ("J2 WINS!")
if ( J1 == "papel" and J2 == "piedra"):
	print ("J1 WINS!")
if ( J1 == J2 ):
	print ("Empate!!")
