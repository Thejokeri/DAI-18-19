import random

numaleatorio =  random.randint(0,10)
num = int(input("Introduzca el valor: "))

while num != numaleatorio:
    if num > numaleatorio:
        print ("Menor")
        num = int(input("Introduzca el valor: "))
    else:
        print ("Mayor")
        num = int(input("Introduzca el valor: "))

print ("Correcto") 