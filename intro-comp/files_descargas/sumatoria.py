#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# (Cuestión técnica.) Python por defecto limita a 1000 la cantidad
# de llamados recursivos, para evitar que se rompa todo en caso de
# agotarse el espacio de stack. Elevo este límite acá, para poder
# mostrar cómo se puede acabar ese espacio.
sys.setrecursionlimit(100000000)

# Calcula (en forma iterativa) la sumatoria entre 1 y n.
def sumatoriaIter(n):
	RV = 0
	while n > 0:
		RV = RV + n
		n = n - 1
	return RV

# Calcula (en forma recursiva) la sumatoria entre 1 y n.
def sumatoriaRec(n):
	if n == 0:
		RV = 0
	else:
		RV = sumatoriaRec(n - 1) + n
	return RV

# Al ir subiendo el valor de n, en algún punto la versión recursiva
# arroja "Segmentation fault (core dumped)" pero la versión iterativa
# termina bien. Esto se debe a que se agota el espacio en el stack 
# para los nuevos llamados recursivos.
x = int(sys.argv[1])
print(sumatoriaIter(x))
print(sumatoriaRec(x))

