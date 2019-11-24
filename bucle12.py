#La suma de los numeros cuando x es menor que y
import os
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
y_invalido=(y<x)
suma=0
while(y_invalido == True):
    y=int(input("ingrese valor:"))
    y_invalido=(y<x)

suma=(x+y)
#fin
print("La suma de los numeros es:", suma)
