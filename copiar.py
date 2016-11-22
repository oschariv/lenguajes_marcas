#!/usr/bin/python3
import os, shutil

RUTA_DIRECTORIO_DESTINO = ".." + os.sep + "oscarmaestre.github.io" + os.sep + "marcas"
RUTA_APUNTES = "_build" + os.sep + "singlehtml"
print ("Borrando " + RUTA_DIRECTORIO_DESTINO)
shutil.rmtree ( RUTA_DIRECTORIO_DESTINO , ignore_errors=True)

shutil.copytree(RUTA_APUNTES, RUTA_DIRECTORIO_DESTINO, ignore=None)