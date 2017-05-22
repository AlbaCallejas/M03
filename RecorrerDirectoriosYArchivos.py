#coding:utf-8
#!/usr/bin/python

import os
 
path_to_explore="./test/"

#Mostrar Directorios 
for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:
   	 print(name)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Mostrar la ruta de los directorios

for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:	 
    	name_path=os.path.join(root, name)                                                          
    	print(name_path)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Mostrar el peso en bytes de los directorios

for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:
            name_path=os.path.join(root, name)
            print(name_path)
            print os.stat(name_path).st_size
