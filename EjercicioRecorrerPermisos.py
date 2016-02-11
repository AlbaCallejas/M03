#coding:utf-8

import os
import stat

path_to_explore="/home/albacallejas/M03/"

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		name_path=os.path.join(root, name)
		print (name_path)
		permissions=stat.S_IMODE(os.stat(name_path).st_mode )
		if (oct(permissions)[-1:]!=0):
			print oct(permissions)
