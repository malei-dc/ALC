#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(A.shape[0])
    U = A.copy()
    for j in range(m):
        for i in range(j+1, n):
            L[i,j]= U[i,j]/U[j,j] # revisar
            U[i,:] = U[i,:] - L[i,j]*U[j,:]
            cant_op += (n-i-1)*2+1 #ponele xd lo que deberia tener de cant ops

    ## hasta aqui
    
    return L, U, cant_op

# Ejercicio 2
def matriz_B(n):
    B = np.eye(n) - np.tril(np.ones((n,n)),-1)
    return B

def gauss(n):
    return ((n*(n+1))/2)


#Ejercicio 3
"""def resolucion_sistema(L, U, b):
    m=L.shape[0]
    n=L.shape[1]

    y = b.copy()

    for i in range(m):
        for j in range(i):
            y[i] += b[j] - L[i, j] * y[j]

    x = y.copy() / U[m-1,m-1]

    for i in range(m-1, -1, -1):
        for j in range(i-1, -1, -1):
            x[i] += (y[j] - U[i, j] * x[j]) / U[i, i]
    
    return x"""

def resolucion_sistema(L, U, b):
    m = L.shape[0]

    # Sustitución hacia adelante: Ly = b
    y = np.zeros_like(b, dtype=float)
    for i in range(m):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Sustitución hacia atrás: Ux = y
    x = np.zeros_like(b, dtype=float)
    for i in range(m-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x


def solucion_final(A, b):
    L, U, _ = elim_gaussiana(A)
    x_res = resolucion_sistema(L, U, b)
    return x_res

def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')

    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

    print("---------- Ejercicio 2 ----------")

    import matplotlib.pyplot as plt
    x = np.arange(1,100,1)
    y = gauss(x)
    plt.plot(x, y, '-r')
    #plt.show()

    print("---------- Ejercicio 3 ----------")

    M = np.array([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
    b = np.array([1, 2, 0])
    print("M = ", M)
    print("b = ", b)
    print("Mx = b -> x = ",solucion_final(M, b))

if __name__ == "__main__":
    main()
    
    