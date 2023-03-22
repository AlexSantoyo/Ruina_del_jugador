#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:24:56 2020

@author: alejandro
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

#Supogamos que el jugador A empieza con n monedas
#B con N-n monedas
# A_n el evento A gana eventualmente
# B_n el evento B gana eventualmente, o A se arruina eventualmente
# p = proba de que A gane la ronda
def ruina(n,N,p):
    """Genera una trayectoria del juego, donde cada lanzamiento tiene prob de 
    éxito p. A comienza con n pesos y B con N-n pesos"""
    a_rw = np.array([n])
    while a_rw[-1]<N and a_rw[-1]>0:
        a_rw = np.append(a_rw, a_rw[-1] + np.random.binomial(1,p)*2-1)
        
    return(a_rw)

#ejemplo    
rui_tray = ruina(5,10,0.5)


# Hagamos una función que estime la proba de ruina para cada n, repitiendo el juego M veces
n=5
N=15
p=0.5
q=1-p
M=1000

#proba de ruina teorica
#si p=0.5

pr_teo= 1 - n/N
#si p!= 0.5
#pr_teo = 1 - (1 -(q/p)**n)/(1 -(q/p)**N)
tray = np.array([])
for i in range(M):
    rui=ruina(n,N,p)
    tray = np.append(tray,rui[-1])
    plt.plot(rui)
pr_est = sum(tray == 0)/M
plt.title('Ruina del Jugador')
plt.xlabel('Tiempo')
plt.ylabel('Trayectorias')
plt.show()
print('La probabilidad teórica es: '+ str(pr_teo))
print('La probabilidad empírica es: '+ str(pr_est))
