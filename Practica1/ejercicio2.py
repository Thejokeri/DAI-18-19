import random
import time
import numpy as np

def MergeSort(m):
    a = m.sort(kind='mergesort')
    return a
def QuickSort(m):
    a = m.sort
    return a
 
matrix = np.random.rand(4,4)
print (matrix)
tiempo_anterior = time.time()

matrix1 = MergeSort(matrix)
tiempo_ejecucion = time.time() - tiempo_anterior
 
print (matrix1) 
print ("Tiempo de ejercucion de Mergesort: " + str(tiempo_ejecucion))

tiempo_anterior = time.time()

matrix2 = QuickSort(matrix)
tiempo_ejecucion = time.time() - tiempo_anterior

print (matrix2) 
print ("Tiempo de ejercucion de Quicksort: " + str(tiempo_ejecucion)) 