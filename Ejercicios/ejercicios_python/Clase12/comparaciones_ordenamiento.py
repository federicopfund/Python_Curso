#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%

# <------------------------------- Importar --------------------------------->
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
#%%
#<--------------------- importar algoritmos de ordenamientos ---------------->
import burbujeo as ob
import orden_insercion as oi
import orden_seleccion as os
import orden_merge as om
#%%
#<-------------------------------- Modulaizar ------------------------------->  
N = 256 # Largo maximo de listas
nums = 1000 # Numeros enteros del 1 a nums
list_comp_ob = [] # Lista de comparaciones de burbujeo
list_comp_oi = [] # Lista de comparaciones de insercion
list_comp_os = [] # Lista de comparaciones de seleccion
list_comp_om = [] # Lista de comparaciones de merge
color = ['r', 'g', 'b', 'cyan']
orden = ['Burbujeo', 'Insercion', 'Seleccion', 'Merge']
#%%
#<--------------------------------- Testeo ---------------------------------->
for n in range(N):
    lista_rd = np.random.random_integers(nums, size = n + 1)
    
    list_comp_ob.append(ob.ord_burbujeo(lista_rd.copy()))
    list_comp_oi.append(oi.ord_insercion(lista_rd.copy()))
    list_comp_os.append(os.ord_seleccion(lista_rd.copy()))
    list_comp_om.append(om.merge_sort(lista_rd.copy())[1])

y = np.array([list_comp_ob, list_comp_oi, list_comp_os, list_comp_om])
x = np.arange(1, N+1, 1)
#%%
#<------------------------------ Plots -------------------------------------->
for i in range(4):
    plt.plot(x, y[i], c = color[i])

plt.xlabel('Largo de lista')
plt.ylabel('Comparaciones')
plt.legend(orden, loc='upper left')

plt.show()
