#coding:utf-8
import os, datetime, time

ruta_a_explorar="./test/"

for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
        fecha_actual=datetime.datetime.now().strftime("%Y-%m-%d")
        fecha_archivo=time.ctime(os.path.getatime(ruta_completa))
        print fecha_actual
        print fecha_archivo
